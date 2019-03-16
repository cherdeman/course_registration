from database.db_connect import connect
from classes.person_builder import StudentBuilder, InstructorBuilder
from classes.person_classes import Student, Instructor
from utils.functions import current_term

# Define queries
select_query = """
				SELECT * 
				FROM {} 
				"""

where_clause = """
				WHERE {} = {}
			   """

grades_query = """
				SELECT g.courseid, c.title, g.sectionid, g.term, g.grade
				FROM grades g
				JOIN course c
				USING(courseid)
				WHERE studentid = {}
				"""

def make_students():
	# call function with no arguments
	conn = connect()
	rs = conn.execute(select_query.format('student'))
	students = rs.fetchall()

	student_obj = {}
	for student in students:
		studentid = student[0]
		firstname = student[1]
		lastname = student[2]
		username = student[3]
		password = student[4]

		pastGrades = {}
		currentCourses = []
		crs = conn.execute(grades_query.format(studentid))
		courses = crs.fetchall()
		for course in courses:
			courseid = course[0]
			title = course[1]
			sectionid = course[2]
			term = course[3]
			grade = course[4]

			if grade is None:
				currentCourses.append(courseid)
			else:
				if term not in pastGrades:
					pastGrades[term] = []
				pastGrades[term].append(list((courseid, title, sectionid, grade)))

		sb = StudentBuilder()
		sb.person = Student()
		sb.getId(studentid)
		sb.getFirstname(firstname)
		sb.getLastname(lastname)
		sb.getUsername(username)
		sb.getPassword(password)
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
		username = instr[4]
		password = instr[5]

		ib = InstructorBuilder()
		ib.person = Instructor()
		ib.getId(instrid)
		ib.getFirstname(firstname)
		ib.getLastname(lastname)
		ib.getUsername(username)
		ib.getPassword(password)
		ib.getDeptCode(dept_code)
		i = ib.getPerson()
		instructor_obj[i._instructorid] = i

	return instructor_obj