	# Registration Mediator
#import person_classes as p
#import course_classes as c

class RegistrationMediator():
	def __init__(self):
		self._student = None #Student(firstname, lastname)
		self._course = None #Course(courseid, title, department, enrollment_limit)
		#self.isCourseAvailable = False

	def getStudent(self, student):
		if self._student is None:
			self._student = student

	def getCourse(self, course):
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
		confirm = input("Are you sure you want to add {}? (y/n)".format(self._course.title))
		if confirm == "y":
			# Only one section in this system, would need to be built out
			self._course.addCourse(self._student._studentid)
			self._student._add(self._course._coursenum)
			print("You are enrolled in {}.".format(self._course.title))
			self._course._reg_mediator = None
			self._student._reg_mediator = None
		else:
			print("Ok, you are NOT be enrolled in {}.".format(self._course.title))
			self._course._reg_mediator = None
			self._student._reg_mediator = None
			return

	def dropCourse(self):
		# check that the student is enrolled in the course
		self.checkEnrollment()

		confirm = input("Are you sure you want to drop {}? (y/n)".format(self._course.title))
		if confirm == "y":
			self._student._drop(self._course._coursenum)
			self._course.dropCourse(self._student._studentid)
			print("You have dropped {}.".format(self._course.title))
			self._course._reg_mediator = None
			self._student._reg_mediator = None
		

	def checkEnrollment(self):
		if self._course._coursenum not in self._student.currentCourses:
			print("You are not enrolled in {} so cannot drop it.".format(self._course.title))
			self._course._reg_mediator = None
			self._student._reg_mediator = None
			return
