from app import db


class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(32), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    time_created = db.Column(db.DateTime, nullable=False, default=db.func.now())
    time_updated = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(16), nullable=False)
    last_name = db.Column(db.String(16), nullable=False)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(65), nullable=False)
    time_created = db.Column(db.DateTime, nullable=False, default=db.func.now())
    time_updated = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

