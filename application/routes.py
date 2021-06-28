from application import app, db



from flask import render_template, url_for, redirect, request
from application.forms import AssignmentsForm, StudentsForm
from application.models import Assignments, Students


@app.route('/')
@app.route('/home')
def home():
    
    all_students = Students.query.all()
    return render_template('index.html', all_students = all_students)


@app.route('/create', methods=['GET', 'POST'])
def create():
    form = StudentsForm()
    if request.method=='POST':
        if form.validate_on_submit():
            Student = Students(
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                age = form.age.data,
                )
            db.session.add(Student)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('create.html', subheading = 'New Student', form=form)


@app.route('/<int:studentID>/assignment-list' , methods=['GET', 'POST'])
def assignmentlist(studentID):
    all_assignments = Assignments.query.filter_by(student_id=studentID)
    return render_template('assignmentlist.html', subheading = "List of Assignments", all_assignments=all_assignments, studentID=studentID)


@app.route('/<int:studentID>/assignment-list/add', methods=['GET','POST'])
def addassignment(studentID):
    form = AssignmentsForm()
    if form.validate_on_submit():
        assignment = Assignments(
            assignment_subject = form.assignment_subject.data,
            assignment_grade = form.assignment_grade.data,
            student_id = studentID
        )
        db.session.add(assignment)
        db.session.commit()
        return redirect(url_for('assignmentlist', studentID=studentID))
    return render_template('addassignment.html', subheading = "Add Assignment", form=form)

@app.route('/<int:studentID>/assignment-list/update/<int:assignmentID>', methods=['GET','POST'])
def update(studentID, assignmentID):
    form = AssignmentsForm()
    assignment = Assignments.query.filter_by(id=assignmentID).first()
    if request.method == 'GET':
        form.assignment_subject.data = assignment.assignment_subject
        form.assignment_grade.data = assignment.assignment_grade
    elif request.method == 'POST':
        assignment.assignment_subject = form.assignment_subject.data
        assignment.assignment_grade = form.assignment_grade.data
        db.session.commit()
        return redirect(url_for('assignmentlist', studentID=studentID))
    return render_template('update.html', subheading='Update Page', assignment=assignment, studentID=studentID, form=form)   


@app.route("/<int:studentID>/assignment-list/delete/<int:assignmentID>" , methods=['GET', 'POST'])
def delete(studentID, assignmentID):
    assignment = Assignments.query.filter_by(id=assignmentID).first()
    db.session.delete(assignment)
    db.session.commit()
    return redirect(url_for('assignmentlist', studentID=studentID))



@app.route("/student_list/delete/<int:id>" , methods=['GET', 'POST'])
def delete_student(id):
    student = Students.query.filter_by(id=id).first()
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('home', id=id))



