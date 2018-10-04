For run application, execute command:
python run.py

or

export FLASK_APP=run.py
set FLASK_APP=ticket

flask run

---
pip install flask-sqlalchemy

pip install flask-migrate

Add config.py file and add delare db config

Int to run app (ticket) import library
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

add config app and db,migrate 
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from ticket import models
---
run "flask db init"
flask db migrate -m "users table"
flask db upgrade
---
install flask login 
pip install flask-login
pip install Flask-WTF
pip install Flask-Babel


-- for gen qr code
pip install Flask-QRcode