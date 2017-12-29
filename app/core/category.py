from app.models import Category
from app.serializers import CategorySchema
from app import db
from config import error_codes as ec
from slugify import slugify


def create(name):
    slug = slugify(name)

    category_schema = CategorySchema()
    new_category, errs = category_schema.load({"name": name, "slug": slug})

    if errs:
        return None, errs

    category = Category.query.filter_by(slug=slug).one_or_none()

    if category:
        return None, ec[409]

    db.session.add(new_category)
    db.session.commit()

    category_data, errs = category_schema.dump(new_category)

    return category_data, errs


def get():
    categories = Category.query.all()

    category_schema = CategorySchema(many=True)
    category_data, errs = category_schema.dump(categories)

    return category_data, errs


def update(cid, name):
    category = Category.query.filter_by(id=cid).one_or_none()

    if not category:
        return None, ec[404]

    category.name = name
    category.slug = slugify(name)
    db.session.commit()

    category_schema = CategorySchema()
    category_data, errs = category_schema.dump(category)

    return category_data, errs


def delete(cid):
    category = Category.query.filter_by(id=cid).one_or_none()

    if not category:
        return None, ec[404]

    db.session.delete(category)
    db.session.commit()

    category_schema = CategorySchema()
    category_data, errs = category_schema.dump(category)

    return category_data, errs
