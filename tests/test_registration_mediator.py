# Registration Mediator Tests

import pytest
from classes.person_classes import *
from classes.course_classes import Course
from classes.registration_mediator import RegistrationMediator

#Test objects
test_student = Student("Claire", "Herdeman")
test_course = Course(1, "Object Oriented Programming", "CS", 30)
test_mediator = RegistrationMediator()

# Tests specific to registration mediator class
def test_mediator_student():
	assert test_mediator._student is None

def test_mediator_course():
	assert test_mediator._course is None

def test_mediator_getStudent():
	test_mediator.getStudent(test_student)
	assert test_mediator._student == test_student

def test_mediator_getCourse():
	test_mediator.getCourse(test_course)
	assert test_mediator._course == test_course

def test_course_getCourse():
	test_course._reg_mediator == test_mediator

def test_course_isCourseAvailable():
	assert test_mediator.isCourseAvailable()

