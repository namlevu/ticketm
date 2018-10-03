from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from ticket import db
from ticket import login

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))

  def __repr__(self):
    return '<User {}>'.format(self.username)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)
  
  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

  @login.user_loader
  def load_user(id):
    return User.query.get(int(id))

class Ticket(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  buyer_email = db.Column(db.String(128), index=True, unique=True)
  buyer_tel = db.Column(db.String(16))
  quanlity = db.Column(db.Integer)
  bought_at = db.Column(db.DateTime())
  amount = db.Column(db.Integer)
  deleted = db.Column(db.Boolean)
  deleted_at = db.Column(db.DateTime())
  created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  updated_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  note = db.Column(db.String(512))

  def __repr__(self):
    return '<Ticket {}><email/phone {}/{}><quanlity/amount {}/{}>'.format(self.id, self.buyer_email, self.buyer_tel, self.quanlity, self.amount)
