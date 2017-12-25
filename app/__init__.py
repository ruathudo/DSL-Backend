import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config


app = Flask(__name__, instance_relative_config=True)

config_name = os.getenv('FLASK_CONFIG')

app.config.from_object(app_config[config_name])
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from . import models

db.create_all()
db.session.commit()


@app.route('/')
def hello_world():
    return 'Hello World!'


