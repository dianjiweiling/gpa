from flask import render_template, session, redirect, url_for, flash
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
        print session['GPA']
        if session['GPA'] > 0:
            session['yes'] = True
            students = Student.query.filter_by(student_id=form.nameid.data).first()
            if students is None:
                print "student is None"
                student = Student(student_id=form.nameid.data)
                info = Info(gpa=session['GPA'], student=student)
                db.session.add_all([student, info])
                db.session.commit()
            else:
                print "-----student------------"
                print type(students)
                print students
                print "-----------------"
        else:
            flash(u'Your ID or Password is WRONG~')
            session['yes'] = False
        return redirect(url_for('.index'))
    return render_template('index.html',form=form, 
                            yes=session.get('yes', False),
                            GPA=session.get('GPA'))
