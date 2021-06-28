from os import name
import unittest
from flask import url_for
from flask.wrappers import Response
from flask_testing import TestCase

from application import app, db 
from application.models import Students, Assignments


class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED= False
            )
        return app

    def setUp(self):   
            db.create_all()
            test_student= Students(
                first_name = "Layek", 
                last_name = "Hakim",
                age = 25 
            )
            test_assignment = Assignments(
                assignment_subject = "English",
                assignment_grade = "A"    
            )
            test_student.assignments.append(test_assignment)
            db.session.add(test_student) 
            db.session.add(test_assignment)
            db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_create_get(self):
        response = self.client.get(url_for('create'))
        self.assertEqual(response.status_code, 200)

    def test_assignmentlist_get(self):
        response = self.client.get(url_for('assignmentlist', studentID=1))
        self.assertEqual(response.status_code, 200)

    def test_addassignment_get(self):
        response = self.client.get(url_for('addassignment', studentID=1))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update', studentID=1, assignmentID=1))
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', studentID=1, assignmentID=1))
        self.assertEqual(response.status_code, 302)

class TestRead(TestBase):
    def test_read_student(self):
        response= self.client.get(url_for("home"))
        self.assertIn(b"Layek", response.data)  
        self.assertIn(b"Hakim", response.data) 

    def test_read_assignmentlist(self):
        response = self.client.get(url_for("assignmentlist" , studentID=1))
        self.assertIn(b"English", response.data) 
        self.assertIn(b"A", response.data) 

    def test_read_update(self):
        response = self.client.get(url_for("update" , studentID=1, assignmentID=1))
        self.assertIn(b"English", response.data) 
        self.assertIn(b"A", response.data) 






