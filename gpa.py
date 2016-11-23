import os
from flask import Flask, render_template

from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap 

from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
print os.path.dirname(__file__)
print basedir
print '--------' 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
class NameForm(Form):
	nameid = StringField('your id?', validators=[Required()])
	passwd = PasswordField('you password?', validators=[Required()])
	submit = SubmitField('Query')

@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	return render_template('index.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)