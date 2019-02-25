# This document contains unit for person-related classes

import pytest
from classes.person_classes import *
#from classes.registration_mediator import RegistrationMediator
from classes.course_classes import Course

# Initialize objects for testing
test_student = Student("Claire", "Herdeman")
test_instructor = Instructor("A", "Professor")
test_faculty = Faculty("B", "Professor")

existing_classes = [test_student, test_instructor]
person_subclasses = [Student, Instructor]

# Parametrized tests for all person  classes
@pytest.mark.parametrize('test_class', existing_classes)
def test_constructor(test_class):
	assert len(test_class.__dict__) > 0

@pytest.mark.parametrize('person_class', person_subclasses)
def test_person_subclass(person_class):
	assert issubclass(person_class, Person)

# Tests specific to student class
def test_student_firstname():
	assert test_student.firstname == "Claire"

def test_student_lastname():
	assert test_student.lastname == "Herdeman"

def test_student_username():
	assert test_student.username == "cherdeman"

def test_student_username():
	assert test_student.password == "temp"

def test_student_id():
	assert test_student.idnum > 100001

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

def test_student_lastname():
	assert test_instructor.lastname == "Professor"

def test_student_username():
	assert test_instructor.username == "aprofessor"

def test_student_id():
	assert test_instructor.password == "temp"

def test_student_id():
	assert test_instructor.idnum > 100002

def test_student_password():
	assert test_instructor._password == "temp"
