# Person class definitions

from abc import ABC

class Person(ABC):
	def __init__(self, firstname, lastname, _id):
		self.firstname = firstname
		self.lastname = lastname
		self.username = self.generateUsername()
		self._id = _id
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
	def __init__():
		pass

	def addCourse():
		pass

	def dropCourse():
		pass

	def viewCourses():
		pass

	def viewGrades():
		pass


class Instructor(Person):
	def __init__():
		pass

	def viewRoster():
		pass

	def updateGrades():
		pass


class Faculty(Instructor):
	def __init__():
		pass

	def manageRequests():
		pass

	def requestRoster():
		pass

	def changeCourseDetails():
		pass