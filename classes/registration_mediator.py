	# Registration Mediator
import startup_functions as s
#import course_classes as c

class RegistrationMediator():
	def __init__(self):
		self._student = None #Student(firstname, lastname)
		self._course = None #Course(courseid, title, department, enrollment_limit)
		#self.isCourseAvailable = False

	def getStudent(self, student):
		if self._student is None:
			self._student = student

	def getCourse(self, courseid):
		# Instatiate course object
		course = s.make_course(courseid)

		# Add mediator to course prior to registration
		course.addMediator(self)

		if self._course is None:
			self._course = course

	def isCourseAvailable(self):
		if self._course.enrollment is None or \
		   self._course.enrollment < self._course.enrollment_limit:
		   return True
		return False

	def addCourse(self):
		# Check conditions
		self.checkRegistration()
		past_courses = self.getPastCourses()
		self.checkCourseHistory(past_courses)
		self.checkPrereqs(past_courses)
		
		confirm = input("Are you sure you want to add {}? (y/n)".format(self._course.title))
		if confirm == "y":
			# Only one section in this system, would need to be built out
			self._course.addCourse(self._student._studentid)
			self._student._add(self._course._coursenum)
			print("You are enrolled in {}.".format(self._course.title))
		else:
			print("Ok, you are NOT be enrolled in {}.".format(self._course.title))
			return

	def getPastCourses(self):
		past_courses = []
		for term in self._student.pastGrades.values():
			for course in term:
				courseid = course[0]
				past_courses.append(courseid)

		return past_courses

	def checkRegistration(self):
		if self._course._coursenum in self._student.currentCourses:
			print("You are already registered for {}".format(self._course.title))
			return

	def checkCourseHistory(self, past_courses):
		if self._course._coursenum in past_courses:
			print("You have already taken {} and cannot re-register.".format(self._course.title))
			return

	def checkPrereqs(self, past_courses):
		taken = [course for course in self._course.prereqs if course in past_courses]
		if len(taken) != len(self._course.prereqs):
			print("You have not completed all of the pre-requisites to register for {}.".format(self._course.title))
			return


	def dropCourse(self):
		# check that the student is enrolled in the course
		check = self.checkEnrollment()

		if check:
			confirm = input("Are you sure you want to drop {}? (y/n)".format(self._course.title))
			if confirm == "y":
				self._student._drop(self._course._coursenum)
				self._course.dropCourse(self._student._studentid)
				print("You have dropped {}.".format(self._course.title))
				#self._course._reg_mediator = None
				#self._student._reg_mediator = None
		

	def checkEnrollment(self):
		if self._course._coursenum not in self._student.currentCourses:
			print("You are not enrolled in {} so cannot drop it.".format(self._course.title))
			#self._course._reg_mediator = None
			#self._student._reg_mediator = None
			return False
		return True
