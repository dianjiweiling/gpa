from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

class NameForm(Form):
	nameid = StringField('your id?', validators=[Required()])
	passwd = PasswordField('you password?', validators=[Required()])
	submit = SubmitField('Query')