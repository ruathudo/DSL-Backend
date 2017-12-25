import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from config import app_config

config_name = os.getenv('FLASK_CONFIG')

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config[config_name])
app.config.from_pyfile('config.py')

# init 3rd party
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

from app import models

# register blueprint
from app.api import api as api_blueprint
app.register_blueprint(api_blueprint)
