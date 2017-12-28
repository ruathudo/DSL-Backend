from marshmallow import fields, validate
from app import ma
from app.models import User, Post, Category


class UserSchema(ma.ModelSchema):
    first_name = fields.Str(validate.Length(max=100, error='INVALID_FIRST_NAME'))
    last_name = fields.Str(validate.Length(max=100, error='INVALID_LAST_NAME'))
    username = fields.Str(required=True, validate=validate.Email(error='INVALID_EMAIL'))
    password = fields.Str(required=True, load_only=True,
                          validate=[validate.Length(min=6, max=30, error='INVALID_PASSWORD')])

    class Meta:
        model = User


class PostSchema(ma.ModelSchema):
    categories = fields.Nested('CategorySchema', many=True, dump_only=True)
    slug = fields.Str(required=False)

    class Meta:
        model = Post
        exclude = ['categories']


class CategorySchema(ma.ModelSchema):
    name = fields.Str(validate.Length(max=100, error='INVALID_CATEGORY'))

    class Meta:
        model = Category
        exclude = ['posts']