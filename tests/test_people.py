# Claire Herdeman
# OOP: Practicum 1
# February 11, 2019

# This document contains preliminary unit tests
import pytest

from classes.person_classes import *


existing_classes = [Person("cherdeman"), Student("cherdeman"), Instructor(), Course(), Section(), Lab(), Building(), Room(), TimeSlot(), Search()]
person_subclasses = [Student, Instructor]
course_subclasses = [Section, Lab]
building_subclasses = [Room]

# Parametrized tests for all classes
@pytest.mark.parametrize('test_class', existing_classes)
def test_constructor(test_class):
	assert len(test_class.__dict__) > 0

@pytest.mark.parametrize('person_class', person_subclasses)
def test_person_subclass(person_class):
	assert issubclass(person_class, Person)

@pytest.mark.parametrize('course_class', course_subclasses)
def test_course_subclass(course_class):
	assert issubclass(course_class, Course)

@pytest.mark.parametrize('building_class', building_subclasses)
def test_building_subclass(building_class):
	assert issubclass(building_class, Building)

# Tests specific to person class
test_person = Person("cherdeman")

def test_person_name():
	assert hasattr(test_person, 'name')

def test_person_id():
	assert hasattr(test_person, '_id')

def test_person_username():
	assert hasattr(test_person, 'username')

def test_person_password():
	assert hasattr(test_person, 'password')
