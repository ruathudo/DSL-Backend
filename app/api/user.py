from flask import request, jsonify
from app.api import api
from app.core.user import User


@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User()
    result, error = user.register(data)

    if error:
        print(error)
        return jsonify({'success': False, 'error': error})

    return jsonify({'success': True, 'data': result})


@api.route('/login', methods=['POST'])
def login():
    pass
