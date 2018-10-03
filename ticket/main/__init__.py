from flask import Blueprint

bp = Blueprint('main', __name__)

from ticket.main import routes