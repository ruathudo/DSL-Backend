from werkzeug.security import check_password_hash, generate_password_hash

from app.models import User
from app.serializers import UserSchema
from app import db
from config import error_codes as ec
from app.utils import format_schema_errors


def register(data):
    # load data to validate
    user_schema = UserSchema()
    new_user, errs = user_schema.load(data)

    if errs:
        return None, format_schema_errors(errs)

    # check duplicated user
    user = User.query.filter_by(username=data["username"]).one_or_none()
    if user:
        return None, ec[409]

    # generate hash password
    new_user.password = generate_password_hash(data['password'])

    # add to db
    db.session.add(new_user)
    db.session.commit()
    db.session.refresh(new_user)

    # serialize data
    user_data, errs = user_schema.dump(new_user)

    return user_data, format_schema_errors(errs)


def login(username, password):
    # check user
    user = User.query.filter_by(username=username).one_or_none()

    if not user:
        return None, ec[404]
    # check password
    check_password = check_password_hash(user.password, password)

    if not check_password:
        return None, ec[401]
    # serialize data
    user_schema = UserSchema()
    user_data, errs = user_schema.dump(user)

    return user_data, None
