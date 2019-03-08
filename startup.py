from database.db_connect import connect
from classes.person_builder import StudentBuilder, InstructorBuilder
from classes.person_classes import Student, Instructor
from classes.course_classes import Course, Section
from classes.course_builder import CourseBuilder, SectionBuilder
from datetime import datetime

#
select_query = """
				SELECT * 
				FROM {}
				"""

grades_query = """
				SELECT * 
				FROM grades
				WHERE studentid = {}
				"""



def make_students(conn, student_query):
	rs = conn.execute(student_query)
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

def make_courses(conn, course_query):
	rs = conn.execute(course_query)
	courses = rs.fetchall()

	course_obj = {}
	for course in courses:
		courseid = course[0]
		dept = course[1]
		title = course[2]

		cb = CourseBuilder()
		cb.course = Course()
		cb.getId(courseid)
		cb.getTitle(title)
		cb.getDepartment(dept)

		term = term()
		section_query = """
						SELECT * 
						FROM section
						WHERE courseid = {} and term = {}
						""".format(courseid, term)

		sections = 

def make_sections(conn, section_query):
	rs = conn.execute(section_query)
	sections = rs.fetchall()

	section_obj = {}
	for section in sections
		sectionid = section[0]
		courseid = section[1]
		term = section[2]
		instructorid = section[3]
		enrollment_min = section[4]
		enrollment_max = section[5]
		time = section[6]
		location = section[7]

		sb = SectionBuilder()
		sb.section = Section()
		sb.getId(sectionid)
		sb.getTerm(term)
		sb.getInstructor(instructorid)
		sb.getEnrollmentMin(enrollment_min)
		sb.getEnrollmentMax(enrollment_max)
		sb.getTime(time)
		sb.getLocation(location)
		s = sb.getItem()
		section_obj[s._sectionid] = s

	return section_obj

def term():
	year = datetime.now().year
	month = datetime.now().month
	if month < 7:
		term = "spr"
	else:
		term = "fall"

	return term + str(year)


def main():
	conn = connect()
	students = make_students(conn, select_query.format('student'))
	print("made students {}".format(students.keys()))
	instructors = make_instructors(conn, select_query.format('instructor'))
	print("made instructors {}".format(instructors.keys()))

if __name__ == "__main__":
	main()

