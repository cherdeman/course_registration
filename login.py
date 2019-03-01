from database.db_connect import connect
from startup import make_students


def login():
	conn = connect()
	# only allow login as student for the time being
	username_query = """SELECT username, password, studentid FROM student""" #, "student" FROM student 
				#UNION SELECT username, password, instructorid, "instructor" FROM instructor"""

	rs = conn.execute(username_query)
	usernames = rs.fetchall()

	username = input("Please enter your username: ")
	user = [u for u in usernames if u[0] == username]
	if len(user) > 0:
		user = user[0]
		password = input("Please enter your password: ")
		if password == user[1]:
			students = make_students()
			student = students[user[2]]
			print("Hi {}, welcome to REGIE!".format(student.firstname))
			select_string = "What would you like to do? \nPlease enter the number of the option you'd like to select: \n" + \
			"1) change password "
			select = input(select_string)
			if int(select) == 1:
				student.changePassword()

		else:
			print("I'm sorry, that password is incorrect.")
			return
	else:
		print("I'm sorry, that username is incorrect.")


def main():
	login()

if __name__ == "__main__":
	main()




