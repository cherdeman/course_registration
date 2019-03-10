from abc import ABC, abstractmethod
from classes.course_classes import Course, Section
from datetime import datetime

class Builder(ABC):
	def __init__(self):
		pass
    
	@abstractmethod
	def getId():
		pass

	@abstractmethod
	def getItem(self):
		pass

class CourseBuilder(Builder):
	def __init__(self):
		self.course = None

	def getId(self, coursenum):
		self.course._coursenum = coursenum

	def getTitle(self, title):
		self.course.title = title

	def getDepartment(self, dept):
		self.course.department = dept

	def getSections(self, section):
		self.course.section = section

	def getEnrollmentUpdates(self):
		self.course.updateEnrollment()
		self.course.enrollmentLimit()

	def getItem(self):
		return self.course


class SectionBuilder(Builder):
	def __init__(self):
		self.section = None

	def getId(self, sectionid):
		self.section._sectionid = sectionid

	def getTerm(self, term):
		self.section.term = term

	def getInstructor(self, instructorid):
		self.section.instructor = instructorid

	def getEnrollmentMin(self, emin):
		self.section.enrollment_min = emin

	def getEnrollmentMax(self, emax):
		self.section.enrollment_max = emax

	def getEnrollment(self, enrollment):
		self.section.enrollment = enrollment

	def getTime(self, time):
		self.section.time = time

	def getLocation(self, location):
		self.section.location = location

	def getItem(self):
		return self.section


