# Course class definitions

class Course:
	def __init__(self, _id, title, department, enrollment_limit):
		self._id = _id# the course number
		self.title = title
		self.department = department
		#self.faculty = Faculty()
		self.enrollment_limit = enrollment_limit
		self._reg_mediator = None
		self.description = None
		self.instructor = None
		self.enrollees = None
		self.location = None
		self.time = None
		self.prereqs = None

	def addCourse(self, _id):
		if self.enrollees is None:
			self.enrollees = []
		self.enrollees.append(_id)


	def dropCourse(self, studentid):
		self.enrollees.remove(studentid)
		if len(self.enrollees) == 0:
			self.enrollees = None

	def addMediator(self, reg_mediator):
		if self._reg_mediator is None:
			self._reg_mediator = reg_mediator

	def addInstructor():
		pass

class Section:
	def __init__(self):
		pass

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