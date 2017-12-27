from app import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(16), nullable=False)
    last_name = db.Column(db.String(16), nullable=False)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.Enum('admin', 'member'))
    time_created = db.Column(db.DateTime, nullable=False, default=db.func.now())
    time_updated = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())


class Category(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    # posts = db.relationship('Post', secondary='post_category', backref='categories', lazy='dynamic')


class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(250), nullable=False)
    slug = db.Column(db.String(250), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    content_md = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum('public', 'private', 'draft', 'trash'))
    categories = db.relationship('Category', secondary='post_category', backref='posts', lazy='dynamic')
    time_created = db.Column(db.DateTime, nullable=False, default=db.func.now())
    time_updated = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())


post_category = db.Table('post_category',
                         db.Column('post_id', db.Integer, db.ForeignKey('post.id', ondelete='CASCADE')),
                         db.Column('category_id', db.Integer, db.ForeignKey('category.id', ondelete='CASCADE'))
                         )
