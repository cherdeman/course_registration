from database.db_connect import connect
from classes.person_builder import StudentBuilder, InstructorBuilder
from classes.person_classes import Student, Instructor

#
student_query = """
				SELECT * 
				FROM student
				"""

courses_query = """
				SELECT * 
				FROM grades
				WHERE studentid = {}
				"""

def make_students(conn, student_query, courses_query):

	rs = conn.execute(student_query)
	students = rs.fetchall()

	student_obj = {}
	for student in students:
		studentid = student[0]
		firstname = student[1]
		lastname = student[2]

		pastGrades = {}
		currentCourses = []
		crs = conn.execute(courses_query.format(studentid))
		courses = crs.fetchall()
		for course in courses:
			courseid = course[1]
			sectionid = course[2]
			term = course[3]
			grade = course[4]

			if grade is None:
				currentCourses.append(courseid)
			else:
				if term not in pastGrades:
					pastGrades[term] = []
				pastGrades[term].append((courseid, sectionid, grade))

		sb = StudentBuilder()
		sb.person = Student()
		sb.getFirstname(firstname)
		sb.getLastname(lastname)
		sb.getUsername()
		sb.getPassword()
		sb.getId(studentid)
		sb.getPastGrades(pastGrades)
		sb.getCurrentCourses(currentCourses)
		s = sb.getPerson()
		student_obj[s._studentid] = s

	return student_obj

def main():
	conn = connect()
	students = make_students(conn, student_query, courses_query)
	print("made students {}".format(students.keys()))
	print(students[100001].username)

if __name__ == "__main__":
	main()

