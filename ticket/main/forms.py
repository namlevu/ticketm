from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, HiddenField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
#from flask_babel import _, lazy_gettext as _l

class NewTicketForm(FlaskForm):
  buyer_email = StringField('Địa chỉ email', validators=[DataRequired()])
  buyer_tel = StringField('Số điện thoại', validators=[DataRequired()])
  quanlity = IntegerField('Số lượng vé')
  amount = IntegerField('Tổng tiền')
  note = StringField('Ghi chú')
  submit = SubmitField('Created')