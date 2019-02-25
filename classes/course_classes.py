# Course class definitions

class Course:
	def __init__(self, _id, title, department, enrollment_limit):
		self._id = _id# the course number
		self.title = title
		self.department = department
		self.faculty = Faculty()
		self.enrollment_limit = enrollment_limit
		self.description = None
		self.instructor = None
		self.enrollees = None
		self.location = None
		self.time = None
		self.prereqs = None

	def addCourse(_id):
		if self.enrollees is None:
			self.enrollees = []
		self.enrollees.append(_id)


	def dropCourse(studentid):
		updated_enrollees = [student in self.enrollees if student != studentid]
		if len(updated_enrollees) == 0:
			updated_enrollees = None
		self.enrollees = updated_enrollees

	def addInstructor():
		pass

	def

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