from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)


app.secret_key = b'www.namvl.com@ln'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'auth.login'

from ticket.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')
from ticket.main import bp as main_bp
app.register_blueprint(main_bp)

from ticket import models