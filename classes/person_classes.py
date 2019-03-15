# Person class definitions

from abc import ABC, abstractmethod
from database.db_connect import connect, update, view_courses
import classes.registration_mediator as rm
from tabulate import tabulate

class Person(ABC):
	"""
	This is an abstract Person class that is a super class for all 
	student/instuctor classes
	"""
	def __init__(self): 
		self.firstname = None 
		self.lastname = None 
		self.username = None 
		self._password = None 

	@abstractmethod
	def generateUsername(self):
		return self.firstname[0].lower() + self.lastname.lower()

	@abstractmethod
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
	def __init__(self):
		super(Student, self).__init__()
		self._studentid = None 
		self.currentCourses = None
		self.pastGrades = None 
		self._reg_mediator = None

	# Implementations of abstract methods
	def generateUsername(self, db = True):
		self.username = super().generateUsername()
		if db:
			update(connect(), 'student', 'username', "'" + self.username + "'", 'studentid', self._studentid)

	def changePassword(self, db = True):
		super().changePassword()
		if db:
			update(connect(), 'student', 'password', "'" + self._password + "'", 'studentid', self._studentid)

	# Main add/drop functions
	def addCourse(self, courseid):
		self._addMediator(courseid)

		if self._reg_mediator.isCourseAvailable() and \
		   self.currentCourses is None or len(self.currentCourses) < 3: # leave as 3 for now, should be a var
		   self._reg_mediator.addCourse()

		self._reg_mediator = None

	def dropCourse(self, courseid, drop_all = False):
		self._addMediator(courseid)

		self._reg_mediator.dropCourse()

		if drop_all:
			self._reg_mediator = None

	def dropAllCourses(self):
		courselist = self.currentCourses[:]
		for coursenum in courselist:
			coursenum = int(coursenum)
			print("course to drop", coursenum)
			self.dropCourse(coursenum)
			print("remaining list", self.currentCourses)
			print("full list", courselist)

		self._reg_mediator = None

	# Viewing methods
	def viewCourses(self):
		if len(self.currentCourses) == 0:
			print("You are not registered for any courses this term.")
		else:
			course_input = ', '.join([str(coursenum) for coursenum in self.currentCourses])
			print(course_input)
			print("You are currently enrolled in: ")
			view_courses(connect(), course_input)

	def viewGrades(self):
		header = ["Course ID Num", "Title", "Section ID Num", "Grade"]
		if len(self.pastGrades) == 0:
			print("You have no past grades.")
		else:
			for term, grades in self.pastGrades.items():
				print("Term: {}".format(term))
				print(tabulate(self.pastGrades[term], header))
				print()

	# Search
	#def searchCourses(self):

	#### helper methods ####
	def _add(self, courseid):
		if self.currentCourses is None:
			self.currentCourses = []
		self.currentCourses.append(courseid)

	def _drop(self, courseid):
		self.currentCourses.remove(courseid)
			
	def _addMediator(self, courseid):
		# instantiate mediator
		reg_mediator = rm.RegistrationMediator()
		
		# add mediator to current student
		self._reg_mediator = reg_mediator

		# register course/student with mediator
		self._reg_mediator.getStudent(self)
		self._reg_mediator.getCourse(courseid)


class Instructor(Person):
	def __init__(self): 
		super(Instructor, self).__init__() 
		self._instructorid = None
		self.dept_code = None

	def generateUsername(self):
		self.username = super().generateUsername()
		update(connect(), 'instructor', 'username',  "'" + self.username + "'", 'instructorid', self._instructorid)

	def changePassword(self):
		super().changePassword()
		update(connect(), 'instructor', 'password', "'" + self._password + "'", 'instructorid', self._instructorid)

	def viewRoster():
		pass

	def updateGrades():
		pass


class Faculty(Instructor):
	def __init__(self): 
		super(Faculty, self).__init__() 

	def manageRequests():
		pass

	def requestRoster():
		pass

	def changeCourseDetails():
		pass