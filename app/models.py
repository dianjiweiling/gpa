from . import db 


class Student(db.Model):
	__tablename__ = 'students'
	id = db.Column(db.Integer, primary_key=True)
	student_id = db.Column(db.String(12), unique=True, index=True)
	users = db.relationship('Info', backref='student', lazy='dynamic')

	def __repr__(self):
		return '<Student %r>' % self.name

class Info(db.Model):
	__tablename__ = 'infos'
	id = db.Column(db.Integer, primary_key=True)
	student_name = db.Column(db.String(32))
	gpa = db.Column(db.Float)
	user_id = db.Column(db.Integer, db.ForeignKey('Student.id'))

	def __repr__(self):
		return '<Info %r>' % self.name