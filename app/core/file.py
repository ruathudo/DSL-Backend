import os
from werkzeug.utils import secure_filename
from app.models import File
from app import app
from google.cloud import storage


from config import error_codes


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def upload(file):
    if not file or not allowed_file(file.filename):
        return None, error_codes[400]
    # save file to tmp folder in local
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # create storage client and update from local to cloud
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(app.config['STORAGE_BUCKET'])
        blob = bucket.blob('uploads/' + filename)
        blob.upload_from_filename(file_path)
    except Exception as e:
        return None, e

    # delete file in local when done
    os.remove(file_path)
    url = app.config['STORAGE_URL'] + filename

    return url, None
