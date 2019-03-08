# Course class definitions

from database.db_connect import connect, update

class Course:
	def __init__(self):
		self._coursenum = None
		self.title = None
		self.department = None
		self._reg_mediator = None
		self.enrollment = None
		self.enrollment_limit = None
		self.sections = None

	def addCourse(self, studentid):
		if self.enrollees is None:
			self.enrollees = []
		self.enrollees.append(studentid)


	def dropCourse(self, studentid):
		self.enrollees.remove(studentid)
		if len(self.enrollees) == 0:
			self.enrollees = None

	def addMediator(self, reg_mediator):
		if self._reg_mediator is None:
			self._reg_mediator = reg_mediator

	def updateEnrollment(self):
		enrollment = 0
		for section in self.sections.values():
			enrollment += len(section.enrollment)

		self.enrollment = enrollment

	def enrollmentLimit(self):
		limit = 0
		for section in self.sections.values():
			limit += section.enrollment_max

		self.enrollment_limit = limit


class Section:
	def __init__(self):
		self._sectionid = None
		self.term = None
		self.instructor = None
		self.enrollment_min = None
		self.enrollment_max = None
		self.enrollment = None
		self.time = None
		self.location = None

class Lab:
	def __init__(self):
		pass

class Building:
	def __init__(self):
		pass

class Room:
	def __init__(self):
		pass

class TimeSlot:
	def __init__(self):
		pass

class Search:
	def __init__(self):
		pass