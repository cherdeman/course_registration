from abc import ABC, abstractmethod
from classes.person_classes import Student, Instructor
#from database.db_connect import connect

class Builder(ABC):
	def __init__(self):
		self.person = None

	@abstractmethod
	def getId(): 
		pass

	def getFirstname(self, firstname):
		self.person.firstname = firstname

	def getLastname(self, lastname):
		self.person.lastname = lastname

	def getUsername(self):
		self.person.generateUsername()

	def getPassword(self):
		self.person._password = "temp"

	def getPerson(self):
		return self.person


class StudentBuilder(Builder):
	def getId(self, studentid):
		self.person._studentid = studentid

	def getPastGrades(self, pastGrades):
		self.person.pastGrades = pastGrades

	def getCurrentCourses(self, currentCourses):
		self.person.currentCourses = currentCourses


class InstructorBuilder(Builder):
	def getId(self, instructorid):
		self.person._instructorid = instructorid

	def getDeptCode(self, dept_code):
		self.person.dept_code = dept_code

