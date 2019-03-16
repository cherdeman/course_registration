from database.db_connect import connect
from classes.make_people import make_students#, make_courses\
from classes.search_class import Search

class Login:
	def __init__(self):
		self.verified = False

	def control(self):
		students = make_students()
		#courses = make_courses()
		student_id = self.verifyCredentials()
		if self.verified:
			#courses = make_courses()
			student = students[student_id]
			print("Hi {}, welcome to REGIE!".format(student.firstname))
			self.provideOptions(student)
		else:
			return

	def verifyCredentials(self):
		conn = connect()
		# only allow login as student for the time being
		username_query = """SELECT DISTINCT username, password, studentid FROM student""" 
		rs = conn.execute(username_query)
		usernames = rs.fetchall()

		# Allow 3 attempts to correctly enter username
		user = self.enterUsername(usernames)
		name_count = 1
		while user is None:
			print("Please try again.")
			if name_count == 3:
				print("You have exceeded the number of tries for this session.")
				return
			user = self.enterUsername(usernames)
			name_count += 1
			
		# Allow 3 attempts to correctly enter password
		pass_count = 1
		student_id = self.enterPassword(user)
		while student_id is None:
			print("Please try again.")
			if pass_count == 3:
				print("You have exceeded the number of tries for this session.")
				return
			student_id = self.enterPassword(user)
			pass_count += 1
			
		return student_id

	def enterUsername(self, usernames):
		username = input("Please enter your username: ")
		user = [u for u in usernames if u[0] == username]
		if len(user) == 0:
			print("I'm sorry, that username is incorrect.")
			return
		return user[0] 

	def enterPassword(self, user):
		expected_password = user[1]
		student_id = user[2]
		password = input("Please enter your password: ")
		if password != expected_password:
			print("I'm sorry, that password is incorrect.")
			return
		self.verified = True
		return student_id

	def provideOptions(self, student): #courses
		active = True

		while active:
			print("What would you like to do?")
			print("1) Change Password")
			print("2) Add Course")
			print("3) Drop Course")
			print("4) Drop All Courses")
			print("5) View Past Grades")
			print("6) View Current Courses")
			print("7) Search Courses")
			print("8) Exit")
			option = int(input("Please enter the number of the option you'd like to select: "))
			if option == 1:
				student.changePassword()
			elif option == 2:
				coursenum = int(input("Enter the course number: "))
				student.addCourse(coursenum)
			elif option == 3:
				coursenum = int(input("Enter the course number: "))
				student.dropCourse(coursenum)
			elif option == 4:
				student.dropAllCourses()
			elif option == 5:
				student.viewGrades()
			elif option == 6:
				student.viewCourses()
			elif option == 7:
				Search().control()
			else:
				print("You are exiting the system, bye")
				active = False


def main():
	login = Login()
	login.control()

if __name__ == "__main__":
	main()




