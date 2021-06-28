#    **Assignments**

## Contents
* [Introduction](#introduction)
    * [Objective](#objective)
    * [My project proposal](#My-project-proposal)
* [Architecture](#architecture)
    * [Risk Assessment](#risk-assessment)
    * [Project tracking](#project-tracking)
    * [Entity relationship diagram](#entity-relationship-diagram)
    * [Continuous Integration pipeline](#continuous-integration-pipeline)
* [Crud functionality](#crud-functionality)
    * [create students page](#create-students-page)
    * [main page - assignments list](#main-page---assignments-list)
* [CI server](#ci-server)
* [Testing](#testing)
    * [unit testing](#unit-testing)
    * [integration testing](#integration-testing)
    * [test results](#test-results)
* [Future improvements](#future-improvements)

## Introduction
### Objective:

The objective provided for this project is as follows:

> "To create a CRUD Application with utilisation are supporting tools, methodologies and technologies that encapsulate all core modules covered in during training."

<br/>

More specifically the requirements of the project are as follows:
* A Trello board or equivalent
* A relational database to store data must contain at least one, one to many relationships.
* Clear documentation from a design phase
* Risk assessment
* Functioning CRUD application created in PYTHON.
* Automated test for validation
* Functioning front and website and integrated APIs using flask
* Fully integrated into git or other Version control systems

### My project proposal
The project idea that I decided to design is an assignments list. Assignments list is a web application where students are able to create a list of subjects which they have taken a test for and store their grades as data. The students are able to create a student on an assignment list which they can add a list of assignments to their page which will then be stored automatically into the database with their user ID. They can also update their account by changing the assignments into a different one. Each student can also delete any of their assignments that they added.

And outline of how the CRUD application is implemented can be seen below:

**Create**:
* The web application generates an ID where it will redirect in them back to the homepage.
    * Enter First name
    * Enter last name
    * Age

**Read**:
* The student will be able to add to the assignments list.
   * Add 
   * Enter subject name
   * Enter subject grade

**Update**:
* The student can click on the update button, if the student made a mistake and wanted to change their initial subject/assignment that they added.
    * Update button
    * Enter subject name
    * Enter subject grade

**Delete**:
* A delete button was created in order for the student to be able to delete the subject and the grade or delete the user as a whole.
   * Delete assignment
<br/>

# Architecture
## Risk Assessment

The risk assessment after the final web application.

![After - starting the project](https://github.com/Layekhakim/QA-Fundamentals-Project/blob/main/RISK%20ASSESSMENT%20for%20project1.png)



## Project Tracking
### Trello Board
For the project tracking Trello board was used to keep track of the progress of the project. Personally Trello board was ideal as it is more pleasing to look at and user friendly which was ideal for this type of project. The Trello board was set up with individual list containing elements for that list. The card elements can be moved left to right in order of the progress.

The list I produced are as follows:
* Project requirements - Containing relevant links.
* User stories – Each card in the format & quote;"As a [User]..., I want [Feature], so that... [Details]"
* In progress - Which contains the task that is currently being worked on.
* Complete - All tasks that are completed.
* Tasks I could not complete - This represents the issues that I had faced during the process of this project.


![trello board](https://github.com/Layekhakim/QA-Fundamentals-Project/blob/main/trello.png)
<br/><br/>

### Entity relationship diagram
Pictured below is an entity relationship diagram (ERD) showing the structure of the database. It features a one to many relationship between the Student and Assignments thus the foreign key is in the student_ID column as a result a user can input many subjects.
<br/>

![ERD Diagram](https://github.com/Layekhakim/QA-Fundamentals-Project/blob/main/ERD%20for%20project1.drawio.png)


### Continuous Integration pipeline
The picture below shows a image of a continuous integration pipeline with the associated services relating to them. The development starts with getting tasks from the Trello board. The initial main starting point for this project was using pythons main framework flask. This means that once the PYTHON code using VS code is completed it can be then pushed on to a version control system which in this case I am using Git Hub, which then triggers a web hook. Jenkins then automates the unit and integration tests that shows the developer coverage on the console. The developer can then therefore, assess their report and work on any failed test. After any successful test Jenkins then automatically runs a testing environment for any dynamic testing.
<br/>

![ci pipeline](https://i.imgur.com/bDoWIRq.png)

## CRUD functionality
#### Create Students page
This section will discuss the basic workings of the front end web application design for this project. The navigation to the homepage or to the URL with no specified path, the user will notice a title called assignments list. On the homepage, the student will then notice a button which, if you click the button it will redirect them to a create student page. The way that this works is that once the student clicks on the create student button, a new student is generated in the database with their names written in the required fields. This will then subsequently be shown in the homepage under a subheading called Students due to the name being in the database.


First the create student button is clicked:

* First name
* Last name
* Age

![Create Page](https://github.com/Layekhakim/QA-Fundamentals-Project/blob/main/Createstudent.png)

After the student enters their details, it will redirect them back to the homepage and then the student will see thier name under the subheading 'Students'

![Home Page](https://github.com/Layekhakim/QA-Fundamentals-Project/blob/main/studentslist.png)


#### Main page - assignment list

After creating a student, the student can now click on their own name on the homepage, which will then redirect them to the main page which in this instance it is the list of assignments page.

On the list of the assignments page, the student is then given an option to add assignments. The student will also notice that on this page it is empty as there are no entries initiated. After the student clicks on add assignments, it will redirect them to the add assignments page where the student can at this point submit an assignment subject and grade that they want to store. After entering a assignment name and the grade this information Will be stored on to the database with their unique ID.

![Add assignment](https://github.com/Layekhakim/QA-Fundamentals-Project/blob/main/addassignment.png)

After the student clicks on submit it will then redirect the student back to the assignment list page and there the student will see their subject entry. Also the student can notice that under the assignment they submitted, there are other options to add more assignments in which the student can click on the button to add another entry to do list.

 ![Add assignment](https://github.com/Layekhakim/QA-Fundamentals-Project/blob/main/assignmentsupdate.png)

 The other option is the update button when the student clicks this button underneath the subject that they just submitted, the update to button will redirect the student back to the add assignments page. At this point the student will notice that their initial entry will be shown. From here the student can change their initial assignments entry. This will then redirect the student back to the assignments list page were the updated subject is now there.

![update](https://github.com/Layekhakim/QA-Fundamentals-Project/blob/main/canupdate.png)

After the student has entered all of the assignments and the grades they wish to store, there is an option to delete certain entries or all entries if thats what the student wants to do.

![delete](https://github.com/Layekhakim/QA-Fundamentals-Project/blob/main/assignmentsdeleted.png)

![delete/student](https://github.com/Layekhakim/QA-Fundamentals-Project/blob/main/deletedstudent.png)

### CI Server

![Jenkins]()
could not connect

## Testing
### Unit Testing
The first test initated on the assignment list project was unit testing. The route functions are tested individually with various scenarios. Each function therefore, should return the expected response under each given scenario for it to be deemed a success. Testing in this manner helps the developer find out if any of the function is not working the way it is meant to. These tests could be run automatcally after every Git push using Jenkins. Jenkins will then produce a coverage report detailing coverage percentage, whether the tests were successful and which lines have yet to be tested.

### Integration testing
To perform integration testing, Selenium has to be used in this project. I could not complete any Integration testing

### Test Results
I managed to pass less than the bare minimum requirement of Unit Testing, only 41 percent of tests passed.

## Future Improvements
Throughout the course of the project there are many improvements that can be made to the application. Below are a few which I could of developed the web application:
* To improve the front end design of the web application
* Do integration testing and better Unit Testing which will help the developer even more to find any mistakes
* Push it up to the CI server would save a lot of time for the developer for future improvements
* My images do not display on this readme file.
* I could not get the app to run on Jenkins, which was a huge dissapointment
* Complete some labs on QA Learning

### Author
Layek Hakim

### Acknowledgements
Luke Benson - In the 2 weeks of Luke teaching, I have made huge progress.
