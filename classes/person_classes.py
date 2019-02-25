# Person class definitions

from abc import ABC
from registration_mediator import RegistrationMediator

class Person(ABC):
	idnum = 100000

	def __init__(self, firstname, lastname):
		Person.idnum += 1
		self.firstname = firstname
		self.lastname = lastname
		self.username = self.generateUsername()
		self._password = 'temp'

	def generateUsername(self):
		return self.firstname[0].lower() + self.lastname.lower()

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
	def __init__(self, firstname, lastname):
		super(Student, self).__init__(firstname, lastname)
		# instantiating mediator first won't make sense in practice!
		# Needs to make sense how to find the course object
		self._reg_mediator = None
		self.currentCourses = None

	def addCourse(self, course_obj):
		self.addMediator(course_obj)

		if self._reg_mediator.isCourseAvailable() and \
		   self.currentCourses is None or self.currentCourses < 3: # leave as 3 for now, should be a var and based on FT/PT
		   self._reg_mediator.addCourse()

	def dropCourse(self, course_obj):
		self.addMediator(course_obj)
		
		self._reg_mediator.dropCourse()

	def _add(self, courseid):
		if self.currentCourses is None:
			self.currentCourses = []
		self.currentCourses.append(courseid)

	def _drop(self, courseid):
		updated_courses = [course for course in self.currentCourses if course != courseid]
		if len(updated_courses) == 0:
			updated_courses = None
		self.currentCourses = updated_courses

	def dropAllCourses(self, course_obj):
		self.addMediator(course_obj)

		for course in self.currentCourses:
			self._reg_mediator.dropCourse()

	def viewCourses():
		pass

	def viewGrades():
		pass

	def addMediator(self, course_obj):
		reg_mediator = RegistrationMediator()
		#this line at least needs to be called elsewhere
		course_obj.addMediator(reg_mediator)
		
		if self._reg_mediator is None:
			self._reg_mediator = reg_mediator

		reg_mediator.getStudent(self)
		reg_mediator.getCourse(course_obj)


class Instructor(Person):
	def __init__(self, firstname, lastname, _id):
		super(Instructor, self).__init__(firstname, lastname, _id)

	def viewRoster():
		pass

	def updateGrades():
		pass


class Faculty(Instructor):
	def __init__(self, firstname, lastname, _id):
		super(Faculty, self).__init__(firstname, lastname, _id)

	def manageRequests():
		pass

	def requestRoster():
		pass

	def changeCourseDetails():
		pass