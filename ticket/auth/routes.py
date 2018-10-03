from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from ticket.auth.forms import LoginForm
from ticket.auth import bp
from ticket.models import User

@bp.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('main.index'))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user is None or not user.check_password(form.password.data):
      flash('Invalid username or password')
      return redirect(url_for('auth.login'))
    login_user(user, remember=form.remember_me.data)
    return redirect(url_for('main.index'))

  return render_template('home/login.html', title='Sign In', form=form)

@bp.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('main.index'))