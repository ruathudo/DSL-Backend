from app import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.Enum('admin', 'member'), default='member')
    time_created = db.Column(db.DateTime, nullable=False, default=db.func.now())
    time_updated = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())


class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    # posts = db.relationship('Post', secondary='post_category', backref='categories', lazy='dynamic')


class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(250), nullable=False)
    slug = db.Column(db.String(250), unique=True, nullable=False)
    content = db.Column(db.Text, default='', nullable=False)
    content_html = db.Column(db.Text, default='', nullable=False)
    status = db.Column(db.Enum('public', 'private', 'draft', 'trash'))
    categories = db.relationship('Category', secondary='post_category', backref='posts', lazy='dynamic')
    time_created = db.Column(db.DateTime, nullable=False, default=db.func.now())
    time_updated = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())


post_category = db.Table('post_category',
                         db.Column('post_id', db.Integer, db.ForeignKey('post.id', ondelete='CASCADE')),
                         db.Column('category_id', db.Integer, db.ForeignKey('category.id', ondelete='CASCADE'))
                         )


class File(db.Model):
    __tablename__ = "file"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='SET NULL'), nullable=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('file.id', ondelete='SET NULL'), nullable=True)
    name = db.Column(db.String(250), nullable=False)
    type = db.Column(db.Enum('folder', 'photo', 'video', 'audio', 'pdf', 'txt', 'other'))
    size = db.Column(db.Float, default=0)
    status = db.Column(db.Enum('pending', 'success', 'error', 'trash'))
    time_created = db.Column(db.DateTime, nullable=False, default=db.func.now())
    time_updated = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
