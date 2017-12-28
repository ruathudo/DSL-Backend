from flask import request, jsonify
from app.api import api
from app.core import user


@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user_data, error = user.register(data)

    if error:
        return jsonify({'success': False, 'error': error})

    return jsonify({'success': True, 'data': user_data})


@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_data, error = user.login(data["username"], data["password"])

    if error:
        return jsonify({'success': False, 'error': error})

    return jsonify({'success': True, 'data': user_data})
