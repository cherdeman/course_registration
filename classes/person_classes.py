# Claire Herdeman
# OOP: Practicum 1
# February 11, 2019

# This document is to define mock classes for unit testing

class Person:
	def __init__(self, username):
		self.username = username
		self.id = 000000
		self._password = 'temp'

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

	def searchCourse(self):
		pass

class Instructor:
	def __init__(self):
		pass

class Course:
	def __init__(self):
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