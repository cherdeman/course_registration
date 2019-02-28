# Person class definitions

from abc import ABC
#from database.db_connect import connect

class Person(ABC):
	"""
	This is an abstract Person class that is a super class for all 
	student/instuctor classes
	"""
	# This will generate a unique id for each user in the system
	def __init__(self): #(self, firstname, lastname):
		self.firstname = None #firstname
		self.lastname = None #lastname
		self.username = None #self.generateUsername()
		self._password = None #'temp'

	def generateUsername(self):
		#conn = connect()
		self.username = self.firstname[0].lower() + self.lastname.lower()
		#conn.execute("")



	def changePassword(self):
		option = input("Would you like to change your password? (y/n) ")
		if option == 'y':
			old_pass = input("Please enter your old password: ")
			if old_pass == self._password:
				new_pass = input("Enter a new password: ")
				self._password = new_pass
				print("Password successfully changed!")
				return
			else:
				print("I'm sorry, that's incorrect. Try again.")
				return 
		else:
			print("Ok, nevermind then.")
			return 

class Student(Person):
	"""
	Class representing student
	"""
	def __init__(self): #self, studentid, firstname, lastname, pastGrades):
		super(Student, self).__init__()# firstname, lastname)
		self._studentid = None #studentid
		self.currentCourses = None
		self.pastGrades = None #pastGrades
		self._reg_mediator = None

	def addCourse(self, course_obj):
		self.addMediator(course_obj)

		if self._reg_mediator.isCourseAvailable() and \
		   self.currentCourses is None or len(self.currentCourses) < 3: # leave as 3 for now, should be a var and based on FT/PT
		   self._reg_mediator.addCourse()

	def dropCourse(self, course_obj):
		self.addMediator(course_obj)

		self._reg_mediator.dropCourse()

	def _add(self, courseid):
		if self.currentCourses is None:
			self.currentCourses = []
		self.currentCourses.append(courseid)

	def _drop(self, courseid):
		self.currentCourses.remove(courseid)
		if len(self.currentCourses) == 0:
			self.currentCourses = None

	def dropAllCourses(self, course_obj):
		pass

		# for course in self.currentCourses:
		# 	self._reg_mediator.dropCourse()

	def viewCourses():
		pass

	def viewGrades():
		pass

	def addMediator(self, course_obj):
		# instantiate mediator
		reg_mediator = RegistrationMediator()
		
		# add mediator to current student
		if self._reg_mediator is None:
			self._reg_mediator = reg_mediator

		# register course/student with mediator
		reg_mediator.getStudent(self)
		reg_mediator.getCourse(course_obj)


class Instructor(Person):
	def __init__(self): #self, firstname, lastname, instructorid, dept_code):
		super(Instructor, self).__init__() #firstname, lastname)
		self._instructorid = None
		self.dept_code = None

	def viewRoster():
		pass

	def updateGrades():
		pass


class Faculty(Instructor):
	def __init__(self): #, firstname, lastname):
		super(Faculty, self).__init__() #firstname, lastname)

	def manageRequests():
		pass

	def requestRoster():
		pass

	def changeCourseDetails():
		pass