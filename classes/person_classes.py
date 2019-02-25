# Person class definitions

from abc import ABC

class Person(ABC):
	def __init__(self, firstname, lastname, _id):
		self._id = _id
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

		input("")

class Student(Person):
	def __init__(self, firstname, lastname, _id, reg_mediator):
		super(Student, self).__init__(firstname, lastname, _id)
		self._reg_mediator = reg_mediator
		self.currentCourses = None

	def addCourse(courseid):
		if self._reg_mediator.isCourseAvailable() and \
		   (self.currentCourses is None or self.currentCourses < 3): # leave as 3 for now, should be a var and based on FT/PT
		   self._reg_mediator.addCourse()

	def add(courseid):
		if self.currentCourses is None:
			self.currentCourses = []
		self.currentCourses.append(courseid)

	def drop(courseid):
		updated_courses = [course in self.currentCourses if course != courseid]
		if len(updated_courses) == 0:
			updated_courses = None
		self.currentCourses = updated_courses

	def dropAllCourses():

	def viewCourses():
		pass

	def viewGrades():
		pass


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