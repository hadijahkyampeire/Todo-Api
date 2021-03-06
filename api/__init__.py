import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from api.config import app_config

app = Flask(__name__)
CORS(app)

config_name = os.environ.get('APP_SETTINGS', 'development')
app.config.from_object(app_config.get(config_name))

db = SQLAlchemy(app)

from api.todo import todo

app.register_blueprint(todo)
