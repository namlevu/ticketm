from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from datetime import datetime

from ticket.main import bp
from ticket import db

@bp.before_app_request
def before_request():
  if current_user.is_authenticated:
    current_user.last_seen = datetime.utcnow()
    db.session.commit()
    #g.search_form = SearchForm()
  #g.locale = str(get_locale())

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
  # Do some stuff
  return render_template('home/index.html')
