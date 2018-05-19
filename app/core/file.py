import os
import uuid
import logging
from PIL import Image
from werkzeug.utils import secure_filename
from app.models import File
from app import app
from google.cloud import storage


from config import error_codes


def allowed_extension(filename):
    if '.' not in filename:
        return None

    extension = filename.rsplit('.', 1)[1].lower()

    if extension not in app.config['ALLOWED_EXTENSIONS']:
        return None

    return extension


def upload(file):
    """
    Upload to local
    :return file{name, url, size, ext}
    """
    # check the file extension
    ext = allowed_extension(file.filename)

    if not file or not ext:
        return None, error_codes[400]

    # save file to tmp folder in local
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    try:
        file.save(file_path)
    except IOError:
        logging.exception("File upload to local error: %s", file_path)
        return None, error_codes(500)

    # get the size of file before upload to cloud
    size = os.stat(file_path).st_size

    # upload from local to cloud, this will delete local file after upload success
    url = upload_cloud(file_path, ext)
    if not url:
        return None, error_codes(500)

    return {'name': filename, 'url': url, 'size': size, 'ext': ext}, None


def upload_cloud(path, ext):
    # create storage client and upload from local to cloud
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(app.config['STORAGE_BUCKET'])
        # create unique name for storing to cloud
        unique_name = str(uuid.uuid1()) + '.' + ext
        blob = bucket.blob('uploads/' + unique_name)
        # upload to cloud
        blob.upload_from_filename(path)
    except Exception:
        logging.exception("File upload to cloud error: %s", path)
        return None

    # Delete file in local when done
    os.remove(path)
    url = 'uploads/' + unique_name

    return url


# def resize_image(file):
#     try:
#         im = Image.open(file)
#         im.thumbnail(size, Image.ANTIALIAS)
#         im.save(outfile, "JPEG")
#     except IOError:
#         return None
#     return []


def create_file(user_id=0, folder_id=None, file=None):
    data = {
        'user_id': user_id,
        'folder_id': folder_id,
        'name': file['name'],
        'url': file['url'],
        'size': file['size']
    }

    if file['extension'] in ('png', 'jpg', 'jpeg'):
        pass

    new_file = File(user_id)

    return 'ok', None
