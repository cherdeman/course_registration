import pytest
from classes.course_classes import *
from classes.registration_mediator import RegistrationMediator

# Initialize objects for testing
test_course = Course(1, "Object Oriented Programming", "CS", 30)
existing_classes = [test_course] #, Section(), Lab(), Building(), Room(), TimeSlot(), Search()]
#course_subclasses = [Section, Lab]
#building_subclasses = [Room]

# Parametrized tests for all course classes
@pytest.mark.parametrize('test_class', existing_classes)
def test_constructor(test_class):
	assert len(test_class.__dict__) > 0

# @pytest.mark.parametrize('course_class', course_subclasses)
# def test_course_subclass(course_class):
# 	assert issubclass(course_class, Course)

# @pytest.mark.parametrize('building_class', building_subclasses)
# def test_building_subclass(building_class):
# 	assert issubclass(building_class, Building)

# Test for course class
def test_course_id():
	assert test_course._id == 1

def test_course_title():
	assert test_course.title == "Object Oriented Programming"

def test_course_department():
	assert test_course.department == "CS"

def test_course_enrollment_limit():
	assert test_course.enrollment_limit == 30

def test_course_addCourse():
	test_course.addCourse(1)
	assert test_course.enrollees == [1]

def test_course_dropCourse():
	test_course.dropCourse(1)
	assert test_course.enrollees is None

def test_course_addMediator():
	test_mediator = RegistrationMediator()
	test_course.addMediator(test_mediator)
	assert test_course._reg_mediator == test_mediator