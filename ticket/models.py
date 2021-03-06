from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from ticket import db
from ticket import login

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  disabled = db.Column(db.Boolean, default=False)

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
  unique_id = db.Column(db.String(32), primary_key=True)
  buyer_email = db.Column(db.String(128))
  buyer_tel = db.Column(db.String(16))
  quanlity = db.Column(db.Integer)
  amount = db.Column(db.Integer)
  paid = db.Column(db.Boolean, default=False)
  paid_at = db.Column(db.DateTime())  
  deleted = db.Column(db.Boolean, default=False)
  deleted_at = db.Column(db.DateTime())
  created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  updated_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  created_at = db.Column(db.DateTime())
  updated_at = db.Column(db.DateTime())
  note = db.Column(db.String(512))

  def __repr__(self):
    return 'id:{}, buyer_email:{}, buyer_tel:{}, quanlity:{}, amount:{}>'.format(self.id, self.buyer_email, self.buyer_tel, self.quanlity, self.amount)
  def __str__(self):
    return '{},{},{},{},{}'.format(self.unique_id, str(self.buyer_tel).ljust(16), str(self.quanlity).ljust(2), self.paid, self.note.ljust(9))
