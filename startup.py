from database.db_connect import connect
from classes.person_builder import StudentBuilder, InstructorBuilder
from classes.person_classes import Student, Instructor

#
person_query = """
				SELECT * 
				FROM {}
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

def make_instructors(conn, instructor_query):
	rs = conn.execute(instructor_query)
	instructors = rs.fetchall()

	instructor_obj = {}
	for instr in instructors:
		instrid = instr[0]
		firstname = instr[1]
		lastname = instr[2]
		dept_code = instr[3]

		ib = InstructorBuilder()
		ib.person = Instructor()
		ib.getFirstname(firstname)
		ib.getLastname(lastname)
		ib.getUsername()
		ib.getPassword()
		ib.getId(instrid)
		ib.getDeptCode(dept_code)
		i = ib.getPerson()
		instructor_obj[i._instructorid] = i

	return instructor_obj


def main():
	conn = connect()
	students = make_students(conn, person_query.format('student'), courses_query)
	#print("made students {}".format(students.keys()))
	#print(students[100001].username)
	instructors = make_instructors(conn, person_query.format('instructor'))
	#print("made instructors {}".format(instructors.keys()))

if __name__ == "__main__":
	main()

