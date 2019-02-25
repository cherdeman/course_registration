import pytest
from classes.course_classes import *

# Initialize objects for testing
existing_classes = [Course(1, "Object Oriented Programming", "CS", 30)] #, Section(), Lab(), Building(), Room(), TimeSlot(), Search()]
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