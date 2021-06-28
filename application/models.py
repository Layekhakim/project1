from application import db

class Students(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30),nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    age = db.Column(db.Integer,nullable= False)
    assignments = db.relationship('Assignments', backref='students')
    
class Assignments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    assignment_subject = db.Column(db.String(30), default = False)
    assignment_grade = db.Column(db.String(30), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable = False)