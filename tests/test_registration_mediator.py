# Registration Mediator Tests

import pytest
from classes.person_builder import StudentBuilder
from classes.person_classes import Student, Instructor
from classes.course_classes import Course
from classes.registration_mediator import RegistrationMediator
from classes.course_builder import CourseBuilder, SectionBuilder

#Test objects
sb = StudentBuilder()
sb.person = Student()
sb.getFirstname("Claire")
sb.getLastname("Herdeman")
sb.getUsername("cherdeman")
sb.getPassword("temp")
sb.getId(100000)
sb.getPastGrades({'fall18': (1, 10, "B")})
sb.getCurrentCourses([])
test_student = sb.getPerson()

cb = CourseBuilder()
cb.course = Course()
cb.getId(1)
cb.getTitle("Object Oriented Programming")
cb.getDepartment("CS")
cb.getSections({})
#cb.getEnrollmentUpdates()
cb.getPrereqs([0])
test_course = cb.getItem()

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
	test_mediator.getCourse(test_course, True)
	assert test_mediator._course == test_course

def test_student_mediator():
	test_student._reg_mediator == test_mediator

def test_course_mediator():
	test_course._reg_mediator == test_mediator

# def test_course_isCourseAvailable():
# 	assert test_mediator.isCourseAvailable()

