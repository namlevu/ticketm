from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from datetime import datetime
from Crypto.Cipher import AES
import base64

from ticket.main import bp
from ticket import db
from ticket.main.forms import NewTicketForm
from ticket.models import Ticket

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


@bp.route('/ticket/new', methods=['GET', 'POST'])
@login_required
def newticket():
  form = NewTicketForm()
  if form.validate_on_submit():
    theticket = Ticket.query.filter_by(buyer_email=form.buyer_email.data).first()
    if theticket is None:
      theticket = Ticket(buyer_email=form.buyer_email.data, 
                          buyer_tel= form.buyer_tel.data, 
                          quanlity= form.quanlity.data, 
                          amount= form.amount.data, 
                          note= form.note.data, 
                          created_at = datetime.utcnow(),
                          updated_at = datetime.utcnow(),
                          created_by = current_user.id,
                          updated_by = current_user.id
                          )
      db.session.add(theticket)
      db.session.commit()
      
      from ticket import app
      cipher = AES.new(app.secret_key,AES.MODE_ECB)
      encoded = base64.b64encode(cipher.encrypt(str(theticket)))

      return redirect(url_for('main.genticket',data=encoded),code=55)
    else:
      flask("Người này đã mua vé rồi")

  return render_template('ticket/new.html', form=form)

@bp.route('/ticket/generate', methods=['GET', 'POST'])
@login_required
def genticket():
  # TODO: 
  from ticket import app
  cipher = AES.new(app.secret_key,AES.MODE_ECB)
  encoded = request.data.get('data')
  decoded = cipher.decrypt(base64.b64decode(encoded))

  return render_template('ticket/new.html', message=decoded)