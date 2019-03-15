import pytest
from classes.course_classes import Course, Section
import classes.registration_mediator as rm #import RegistrationMediator
from classes.course_builder import CourseBuilder, SectionBuilder

# Test section builder and generate test_section
sb = SectionBuilder()
sb.section = Section()
sb.getId(10)
def test_sb_getid():
	assert sb.section._sectionid == 10

sb.getTerm("fall2018")
def test_sb_getterm():
	assert sb.section.term == "fall2018"

sb.getInstructor(1)
def test_sb_getinstructor():
	assert sb.section.instructor == 1

sb.getEnrollmentMin(5)
def test_sb_getenrollmentmin():
	assert sb.section.enrollment_min == 5

sb.getEnrollmentMax(30)
def test_sb_getenrollmentmin():
	assert sb.section.enrollment_max == 30

sb.getEnrollment([100001])
def test_sb_getenrollment():
	assert sb.section.enrollment == [100001]

sb.getTime("12:00 - 1:20")
def test_sb_gettime():
	assert sb.section.time == "12:00 - 1:20"

sb.getLocation("RYE")
def test_sb_getlocation():
	assert sb.section.location == "RYE"

# generate test section item
test_section = sb.getItem()

# Test section methods
def test_section_addSection():
	test_section.addSection(100002, 1100, False)
	test_section.enrollment == [100001, 100002]

def test_section_dropSection():
	test_section.dropSection(100002, False)
	test_section.enrollment == [100001]

# Test course builder and get test_builder
cb = CourseBuilder()
cb.course = Course()
cb.getId(1)
def test_cb_getId():
	cb.course._coursenum == 1

cb.getTitle("Object Oriented Programming")
def test_cb_getTitle():
	cb.course.title == "Object Oriented Programming"

cb.getDepartment("CS")
def test_cb_getDepartment():
	cb.course.department == "CS"

cb.getSections(test_section)
def test_cb_getSections():
	cb.course.section == test_section

cb.getEnrollmentUpdates()
def test_cb_getEnrollmentUpdates():
	cb.course.enrollment == 1

test_course = cb.getItem()

# Test for course class
def test_course_coursenum():
	assert test_course._coursenum == 1

def test_course_title():
	assert test_course.title == "Object Oriented Programming"

def test_course_department():
	assert test_course.department == "CS"

def test_course_enrollment_limit():
	assert test_course.enrollment_limit == 30

def test_course_section():
	assert test_course.section == test_section

def test_course_addCourse():
	test_course.addCourse(100002, db = False)
	assert test_course.section.enrollment == [100001, 100002]

def test_course_updateEnrollment_1():
	test_course.updateEnrollment()
	test_course.enrollment == 2

def test_course_dropCourse():
	test_course.dropCourse(100002, db = False)
	assert test_course.section.enrollment == [100001]
	assert test_course.enrollment == 1

def test_course_addMediator():
	test_mediator = rm.RegistrationMediator()
	test_course.addMediator(test_mediator)
	assert test_course._reg_mediator == test_mediator

existing_classes = [test_course, test_section] #, Section(), Lab(), Building(), Room(), TimeSlot(), Search()]
#course_subclasses = [Section, Lab]
#building_subclasses = [Room]

# Parametrized tests for all course classes
@pytest.mark.parametrize('test_class', existing_classes)
def test_constructor(test_class):
	assert len(test_class.__dict__) > 0