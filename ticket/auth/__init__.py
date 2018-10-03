from flask import Blueprint

bp = Blueprint('auth', __name__)

from ticket.auth import routes