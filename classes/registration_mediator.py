# Registration Mediator
from classes.make_courses import make_course

class RegistrationMediator():
	"""
	Mediator between course and student objects
	that facilitates the registration process
	"""
	def __init__(self):
		self._student = None 
		self._course = None 
		
	# Register student and course
	def getStudent(self, student):
		if self._student is None:
			self._student = student

	def getCourse(self, courseid, test = False):
		# Instatiate course object
		if test:
			course = courseid
		else:
			course = make_course(courseid)

		if course is None:
			print("I'm sorry, that is not a valid course number.")
			return False
		else:	
			# Add mediator to course prior to registration
			course._addMediator(self)

			if self._course is None:
				self._course = course
			
			return True

	def isCourseAvailable(self):
		# check course availability 
		if self._course.enrollment < self._course.enrollment_limit:
		   return True
		return False

	def addCourse(self):
		# Check conditions for registration
		reg = self._checkRegistration()
		past_courses = self._getPastCourses()
		hist = self._checkCourseHistory(past_courses)
		prereqs = self._checkPrereqs(past_courses)
		
		if reg and hist and prereqs:
			# confirm and enroll
			confirm = input("Are you sure you want to add {}? (y/n) ".format(self._course.title))
			if confirm.lower() in ["y", "yes"]:
				self._course.addCourse(self._student._studentid)
				self._student._add(self._course._coursenum)
				print("You are enrolled in {}.".format(self._course.title))
			elif confirm.lower() in ["n", "no"]:
				print("Ok, you are NOT enrolled in {}.".format(self._course.title))
				return
			else:
				print("I'm sorry, I don't recognize that input.")
				return
		else:
			print("You do not able to enroll in this course at this time.")


	def dropCourse(self):
		# check that the student is enrolled in the course
		check = self._checkEnrollment()

		if check:
			confirm = input("Are you sure you want to drop {}? (y/n) ".format(self._course.title))
			if confirm.lower() in ["y", "yes"]:
				self._student._drop(self._course._coursenum)
				self._course.dropCourse(self._student._studentid)
				print("You have dropped {}.".format(self._course.title))
			elif confirm.lower() in ["n", "no"]:
				print("Ok, you did NOT drop {}.".format(self._course.title))
			else:
				print("I'm sorry, I don't recognize that input.")

	#### Helper methods ####
	def _getPastCourses(self):
		past_courses = []
		for term in self._student.pastGrades.values():
			for course in term:
				courseid = course[0]
				past_courses.append(courseid)

		return past_courses

	def _checkRegistration(self):
		if self._course._coursenum in self._student.currentCourses:
			print("You are already registered for {}".format(self._course.title))
			return False
		return True

	def _checkCourseHistory(self, past_courses):
		if self._course._coursenum in past_courses:
			print("You have already taken {} and cannot re-register.".format(self._course.title))
			return False
		return True

	def _checkPrereqs(self, past_courses):
		taken = [course for course in self._course.prereqs if course in past_courses]
		if len(taken) != len(self._course.prereqs):
			print("You have not completed all of the pre-requisites to register for {}.".format(self._course.title))
			return False
		return True
		
	def _checkEnrollment(self):
		if self._course._coursenum not in self._student.currentCourses:
			print("You are not enrolled in {} so cannot drop it.".format(self._course.title))
			return False
		return True
