from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from datetime import datetime
import uuid

from ticket.main import bp
from ticket import db, app
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
      theticket = Ticket(
                          unique_id = str(uuid.uuid4().hex),
                          buyer_email=form.buyer_email.data, 
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
      db.session.flush()
      ticket_id =  theticket.unique_id
      db.session.commit()

      return redirect(url_for('main.genticket',data=ticket_id),code=307)
    else:
      flask("Người này đã mua vé rồi")

  return render_template('ticket/new.html', form=form)

@bp.route('/ticket/generate', methods=['GET', 'POST'])
@login_required
def genticket():
  # TODO: 
  ticket_id = request.args['data']
  theticket = Ticket.query.filter_by(unique_id=ticket_id).first()
  if theticket is None:
    abort(404)

  url = request.url_root + 'ticket/validate?key=' + ticket_id

  return render_template('ticket/generate.html', validate_url=url)

@bp.route('/ticket/validate', methods=['GET', 'POST'])
def ticketvalidate():
  keyword = request.args['key']
  if keyword is None or len(keyword) == 0 :
    return render_template('ticket/validate.html', message="Ticket key is invalid.")
  theticket = Ticket.query.filter_by(unique_id=keyword).first()
  if theticket is None:
    return render_template('ticket/validate.html', message="Ticket key is invalid.")

  return render_template('ticket/validate.html', message=keyword, ticket=theticket)
