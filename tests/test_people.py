# This document contains unit for person-related classes

import pytest
from classes.person_classes import *
from classes.person_builder import StudentBuilder, InstructorBuilder
import classes.registration_mediator as rm
from classes.course_classes import Course

ib = InstructorBuilder()
ib.person = Instructor()
ib.getFirstname("A")
ib.getLastname("Professor")
ib.getUsername("aprofessor")
ib.getPassword("temp")
ib.getId(200000)
ib.getDeptCode(1)
test_instructor = ib.getPerson()

test_faculty = Faculty()

# Tests for student builder and creation of test object
sb = StudentBuilder()
sb.person = Student()

sb.getFirstname("Claire")
def test_sb_firstname():
	sb.person.firstname == "Claire"

sb.getLastname("Herdeman")
def test_sb_lastname():
	sb.person.lastname == "Herdeman"

# Test generateUsername person method and getUsername builder method
def test_generateUsername():
	sb.person.generateUsername(db = False)
	sb.person.username == "cherdeman"

sb.getUsername("cherdeman")
def test_sb_username():
	sb.person.username == "cherdeman"

sb.getPassword("temp")
def test_sb_username():
	sb.person._password == "temp"

sb.getId(100000)
def test_sb_id():
	sb.person._studentid == 100000

sb.getPastGrades({'fall18': (1, 10, "B")})
def test_sb_pastgrades():
	sb.person.pastGrades == {'fall18': (1, 10, "B")}

sb.getCurrentCourses([])
def test_sb_currentcourses():
	sb.person.currentCourses == []

test_student = sb.getPerson()

# Tests specific to student class
def test_student_firstname():
	assert test_student.firstname == "Claire"

def test_student_lastname():
	assert test_student.lastname == "Herdeman"

def test_student_username():
	assert test_student.username == "cherdeman"

def test_student_id():
	assert test_student._studentid == 100000

def test_student_password():
	assert test_student._password == "temp"

def test_student_add():
	test_student._add(1234)
	assert test_student.currentCourses == [1234]

def test_student_drop():
	test_student._drop(1234)
	assert test_student.currentCourses is None

# def test_student_addMediator():
# 	test_course = Course(1, "Object Oriented Programming", "CS", 30)
# 	test_student.addMediator(test_course)
# 	assert test_student._reg_mediator == RegistrationMediator()

# Tests specific to instructor class
def test_instructor_firstname():
	assert test_instructor.firstname == "A"

def test_instructor_lastname():
	assert test_instructor.lastname == "Professor"

def test_instructor_username():
	assert test_instructor.username == "aprofessor"

def test_instructor_password():
	assert test_instructor._password == "temp"

def test_instructor_id():
	assert test_instructor._instructorid == 200000

def test_instructor_code():
	assert test_instructor.dept_code == 1

existing_classes = [test_student, test_instructor]
person_subclasses = [Student, Instructor]

# Parametrized tests for all person  classes
@pytest.mark.parametrize('test_class', existing_classes)
def test_constructor(test_class):
	assert len(test_class.__dict__) > 0

@pytest.mark.parametrize('person_class', person_subclasses)
def test_person_subclass(person_class):
	assert issubclass(person_class, Person)
