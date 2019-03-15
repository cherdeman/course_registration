# Course class definitions

from database.db_connect import connect, update, add, drop

class Course:
	def __init__(self):
		self._coursenum = None
		self.title = None
		self.department = None
		self._reg_mediator = None
		self.enrollment = None
		self.enrollment_limit = None
		self.section = None
		self.prereqs = None

	def addCourse(self, studentid, db = True):
		self.section.addSection(studentid, self._coursenum, db)
		self.updateEnrollment()
		self._reg_mediator = None

	def dropCourse(self, studentid, db = True):
		self.section.dropSection(studentid, self._coursenum, db)
		self.updateEnrollment()
		self._reg_mediator = None

	def updateEnrollment(self):
		self.enrollment = len(self.section.enrollment)

	def enrollmentLimit(self):
		self.enrollment_limit = self.section.enrollment_max

	def _addMediator(self, reg_mediator):
		if self._reg_mediator is None:
			self._reg_mediator = reg_mediator


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

	def addSection(self, studentid, courseid, db = True):
		if self.enrollment is None:
			self.enrollment = []
		self.enrollment.append(studentid)
		if db:
			value = "("+ str(studentid) + "," + str(courseid) + "," + str(self._sectionid) + ",'" + self.term + "')"
			add(connect(), 'grades', '(studentid, courseid, sectionid, term)',  value)

	def dropSection(self, studentid, coursenum, db = True):
		self.enrollment.remove(studentid)
		if db:
			drop(connect(), studentid, coursenum)

# Stubbed classes
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