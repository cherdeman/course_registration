# Registration Mediator
from classes.person_classes import Student
from classes.course_classes import Course

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
		   len(self._course.enrollment) < self._course.enrollment_limit:
		   return True
		return False

	def addCourse(self):
		confirm = input("Are you sure you want to add {}? (y/n)".format(self._course.title))
		if confirm == "y":
			self._course.addCourse(self._student.idnum)
			self._student._add(self._course._id)
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
		if self._course._id not in self._student.currentCourses:
			print("You are not enrolled in {} so cannot drop it.".format(self._course.title))
			self._course._reg_mediator = None
			self._student._reg_mediator = None
			return

		confirm = input("Are you sure you want to drop {}? (y/n)".format(self._course.title))
		if confirm == "y":
			self._student._drop(self._course._id)
			self._course.dropCourse(self._student.idnum)
			print("You have dropped {}.".format(self._course.title))
			self._course._reg_mediator = None
			self._student._reg_mediator = None
			return
