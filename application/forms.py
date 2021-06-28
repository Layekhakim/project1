from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired

from application.models import Assignments

class AssignmentsForm(FlaskForm):
    
    assignment_subject = StringField('Subject Name',
        validators = [ 
            DataRequired()
        ]
    )
    
    assignment_grade = StringField('Assignment Grade', 
        validators= [
             DataRequired()
        ]
    )
    
    submit = SubmitField('Submit')

class StudentsForm(FlaskForm):
    first_name = StringField('First Name',
        validators = [
            DataRequired()
        ])
    last_name = StringField('Last Name',
        validators = [
            DataRequired()
        ])
    age = IntegerField('Age',
        validators = [ 
            DataRequired()
        ])
    submit = SubmitField('Submit')



