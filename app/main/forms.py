from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required, Length

class NameForm(Form):
	nameid = StringField('your id?', validators=[Required(),Length(12)])
	passwd = PasswordField('you password?', validators=[Required()])
	submit = SubmitField('Query')