from werkzeug.security import check_password_hash, generate_password_hash

from app.models import User as UserModel
from app.serializers import UserSchema
from app import db
from config import error_codes as ec
from app.utils import format_schema_errors


class User(object):

    def __init__(self):
        pass

    def check_exist(self, username):
        user = UserModel.query.filter_by(username=username).one_or_none()

        if not user:
            return False
        return True

    def register(self, data):
        # load data to validate
        user_schema = UserSchema()
        new_user, errs = user_schema.load(data)

        if errs:
            return None, format_schema_errors(errs)

        # check duplicated user
        is_exist = self.check_exist(data['username'])
        if is_exist:
            return None, ec[409]

        # generate hash password
        new_user.password = generate_password_hash(data['password'])

        # add to db
        db.session.add(new_user)
        db.session.commit()
        db.session.refresh(new_user)

        # serialize data
        user_data, errs = user_schema.dump(new_user)

        return user_data, errs

    def login(self, username, password):
        return None
