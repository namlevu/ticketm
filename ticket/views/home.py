from flask import Blueprint, render_template

home = Blueprint('home', __name__, 
                  template_folder='templates', 
                  static_folder='static')

@home.route('/')
def index():
  # Do some stuff
  return render_template('home/index.html')

@home.route('/login')
def login():
  # Do some stuff
  return render_template('home/login.html')

@home.route('/logout')
def logout():
  # Do some stuff
  return render_template('home/logout.html')