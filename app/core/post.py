from app.models import Post, Category, post_category
from app.serializers import PostSchema
from app import db
from config import error_codes as ec
from slugify import slugify
from app.utils import format_schema_errors


def create(uid, data):
    post_schema = PostSchema()
    print(data)
    new_post, errs = post_schema.load(data)

    if errs:
        return None, format_schema_errors(errs)

    new_post.user_id = uid
    # get list categories by ids
    db.session.add(new_post)
    db.session.commit()
    db.session.refresh(new_post)

    categories = Category.query.filter(Category.id.in_(data['categories'])).all()
    for c in categories:
        new_post.categories.append(c)

    new_post.slug = slugify(new_post.title + "-" + str(new_post.id))
    db.session.commit()

    post, errs = post_schema.dump(new_post)

    return post, errs


def get_by_id(pid):
    post = Post.query.filter_by(id=pid).one_or_none()

    if not post:
        return None, ec[404]

    post_schema = PostSchema()
    post_data, errs = post_schema.dump(post)

    return post_data, errs


def get_by_slug(slug):
    posts = Post.query.filter(Post.slug.like(slug)).all()

    if not posts:
        return None, ec[404]

    post_schema = PostSchema(many=True)
    post_data, errs = post_schema.dump(posts)

    return post_data, errs


def get_by_category(cid):
    posts = Post.query.join(post_category).filter(post_category.c.category_id == cid).all()

    if not posts:
        return None, ec[404]

    post_schema = PostSchema(many=True)
    post_data, errs = post_schema.dump(posts)

    return post_data, errs


def update(pid, data):
    post_schema = PostSchema()
    post_model, errs = post_schema.load(data)

    if errs:
        return None, errs

    post = Post.query.filter_by(id=pid).one_or_none()

    if not post:
        return None, ec[409]

    post = db.session.merge(post_model)
    db.session.commit()

    post_data, errs = post_schema.dump(post)

    return post_data, errs


def delete(pid):
    post = Post.query.filter_by(id=pid).one_or_none()

    if not post:
        return None, ec[404]

    db.session.delete(post)
    db.session.commit()

    post_schema = PostSchema()
    post_data, errs = post_schema.dump(post)

    return post_data, errs
