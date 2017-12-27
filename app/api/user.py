from flask import request, jsonify
from app.api import api
from app.core.user import User


@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    result, error = User.register(data)

    if error:
        return jsonify({'success': False, 'error': error})

    return jsonify({'success': True, 'data': result})


@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result, error = User.login(data["username"], data["password"])

    if error:
        return jsonify({'success': False, 'error': error})

    return jsonify({'success': True, 'data': result})
