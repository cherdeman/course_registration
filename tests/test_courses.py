import pytest
from classes.course_classes import Course, Section
from classes.registration_mediator import RegistrationMediator
from classes.course_builder import CourseBuilder, SectionBuilder

# Initialize objects for testing
sb = SectionBuilder()
sb.section = Section()
sb.getId(10)
sb.getTerm("fall2018")
sb.getInstructor(1)
sb.getEnrollmentMin(5)
sb.getEnrollmentMax(30)
sb.getEnrollment([100001])
sb.getTime("12:00 - 1:20")
sb.getLocation("RYE")
s = sb.getItem()


cb = CourseBuilder()
cb.course = Course()
cb.getId(1)
cb.getTitle("Object Oriented Programming")
cb.getDepartment("CS")
cb.getSections(s)
cb.getEnrollmentUpdates()
test_course = cb.getItem()

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
def test_course_coursenum():
	assert test_course._coursenum == 1

def test_course_title():
	assert test_course.title == "Object Oriented Programming"

def test_course_department():
	assert test_course.department == "CS"

def test_course_enrollment_limit():
	assert test_course.enrollment_limit == 30

def test_course_addCourse():
	test_course.addCourse(100002, db = False)
	assert test_course.section.enrollment == [100001, 100002]

def test_course_dropCourse():
	test_course.dropCourse(100002, db = False)
	assert test_course.section.enrollment == [100001]
	assert test_course.enrollment == 1

def test_course_addMediator():
	test_mediator = RegistrationMediator()
	test_course.addMediator(test_mediator)
	assert test_course._reg_mediator == test_mediator