# Registration Mediator
from person_classes import Student
from course_classes import Course

class RegistrationMediator():
	def __init__():
		self._student = Student(self)
		self._course = Course(self)

	def getStudent(self, student):
		self._student = student

	def getCourse(self, course):
		self._course = course

	def isCourseAvailable():
		if self._course.enrollees is None or \
		   len(self._course.enrollees) < self._course.enrollment_limit:
		   return True
		return False

	def addCourse():
		confirm = input("Are you sure you want to add {}? (y/n)".format(self._course.title))
		if confirm == "y":
			self._course.addCourse(self._student._id)
			self._student._add(self._course._id)
			print("You are enrolled in {}.".format(self._course.title))
		else:
			print("Ok, you are NOT be enrolled in {}.".format(self._course.title))
			return

	def dropCourse():
		# check that the student is enrolled in the course
		if self._course._id not in self._student.currentCourses:
			print("You are not enrolled in {} so cannot drop it.".format(self._course.title))
			return

		confirm = input("Are you sure you want to drop {}? (y/n)".format(self._course.title))
		if confirm == "y":
			self._student._drop()
			self._course.dropCourse()
			print("You have dropped {}.".format(self._course.title))
