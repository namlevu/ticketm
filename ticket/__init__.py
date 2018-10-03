from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .views.home import home

app = Flask(__name__)
app.register_blueprint(home)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
