from flask import request, jsonify
from app.api import api
from config import error_codes
from app.core import file as f


@api.route('/upload', methods=['POST'])
def upload():

    if 'file' not in request.files:
        return jsonify({'success': False, 'error': error_codes[400]})

    file = request.files['file']
    print(file)
    if file.filename == '':
        return jsonify({'success': False, 'error': error_codes[422]})

    result, error = f.upload(file)

    if error:
        return jsonify({'success': False, 'error': error})

    return jsonify({'success': True, 'data': result})
