import jwt
from functools import wraps
from threading import Thread
from flask import request, jsonify
from config import error_codes
from app import app
from app.models import User


def format_schema_errors(errs):
    """
    format the errors dictionary to list, select the first error in value list
    :param errs:
    :return: list of errors ["INVALID_STH"]
    """
    for e in errs.values():
        return e[0]


def auth_required(f):
    def decorator(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return jsonify({'success': False, 'error': error_codes[499]})
        try:
            decoded = jwt.decode(token, app.config['SECRET_KEY'])
        except (jwt.InvalidTokenError, jwt.ExpiredSignatureError):
            return jsonify({'success': False, 'error': error_codes[498]})

        # get user from decoded id
        user = User.query.get(decoded['id'])

        if not user:
            return jsonify({'success': False, 'error': error_codes[403]})

        return f(*args, **kwargs)
    return decorator


def run_async(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return decorator
