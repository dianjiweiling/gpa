from flask import render_template, session, redirect, url_for, current_app
from .. import db
# from ..models import User
# from ..email import send_email
from . import main
from .forms import NameForm
from ..models import Student, Info
from ..gpa import GPASpider


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        myspider = GPASpider(form.nameid.data, form.passwd.data)
        session['GPA'] = myspider.spider()
        if session['GPA'] > 0:
            session['yes'] = True
        else:
            session['yes'] = False
        # student = Student.query.filter_by(student_id=form.name.data).first()
        # if student is None:
        #     student = Student(student_id=form.name.data)
        #     db.session.add(student)
        #     session['known'] = False
            
        #     myspider = gpa.GPASpider()
        #     session['GPA'] = myspider.spider()
        # else:
        #     session['GPA'] = Info.query.filter_by(user_id=student).all()[2]
        #     session['known'] = True
        # session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, yes=session.get('yes', False),GPA=session.get('GPA'))
