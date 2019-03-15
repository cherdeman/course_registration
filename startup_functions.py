from database.db_connect import connect
import classes.person_builder as pb #import StudentBuilder, InstructorBuilder
from classes.person_classes import Student, Instructor
from classes.course_classes import Course, Section
from classes.course_builder import CourseBuilder, SectionBuilder
from datetime import datetime

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

section_query = """
				SELECT * 
				FROM section
				WHERE courseid = {} and term = {}
				"""

enrollment_query = """
					SELECT DISTINCT studentid
					FROM grades
					WHERE courseid = {} and term = {} and sectionid = {}
					"""

def make_student(studentid):
	conn = connect()
	query = select_query + where_clause
	rs = conn.execute(query.format('student', 'studentid', studentid))
	student = rs.fetchone()

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

	sb = pb.StudentBuilder()
	sb.person = Student()
	sb.getId(studentid)
	sb.getFirstname(firstname)
	sb.getLastname(lastname)
	sb.getUsername(username)
	sb.getPassword(password)
	sb.getPastGrades(pastGrades)
	sb.getCurrentCourses(currentCourses)
	s = sb.getPerson()
	
	return s

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

		sb = pb.StudentBuilder()
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

		ib = pb.InstructorBuilder()
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

def make_course(courseid):
	conn = connect()
	query = select_query + where_clause
	rs = conn.execute(query.format('course', 'courseid', courseid))
	course = rs.fetchone()

	courseid = course[0]
	dept = course[1]
	title = course[2]

	cb = CourseBuilder()
	cb.course = Course()
	cb.getId(courseid)
	cb.getTitle(title)
	cb.getDepartment(dept)
	cb.getSections(make_sections(conn, section_query, enrollment_query, courseid, "'"+current_term()+"'"))
	cb.getEnrollmentUpdates()
	cb.getPrereqs(prereqs(conn, cb.course._coursenum))
	c = cb.getItem()
	
	return c

# def make_courses():
# 	conn = connect()
# 	rs = conn.execute(select_query.format('course'))
# 	courses = rs.fetchall()

# 	course_obj = {}
# 	for course in courses:
# 		courseid = course[0]
# 		dept = course[1]
# 		title = course[2]

# 		cb = CourseBuilder()
# 		cb.course = Course()
# 		cb.getId(courseid)
# 		cb.getTitle(title)
# 		cb.getDepartment(dept)
# 		cb.getSections(make_sections(conn, section_query, enrollment_query, courseid, "'"+current_term()+"'"))
# 		cb.getEnrollmentUpdates()
# 		cb.getPrereqs(prereqs(conn, cb.course._coursenum))
# 		c = cb.getItem()
# 		course_obj[c._coursenum] = c

# 	return course_obj

def make_sections(conn, section_query, enrollment_query, courseid, current_term):
	rs = conn.execute(section_query.format(courseid, current_term))
	sections = rs.fetchall()

	section_obj = {}
	for section in sections:
		sectionid = section[0]
		courseid = section[1]
		course_term = section[2]
		instructorid = section[3]
		enrollment_min = section[4]
		enrollment_max = section[5]
		time = section[6]
		location = section[7]

		sb = SectionBuilder()
		sb.section = Section()
		sb.getId(sectionid)
		sb.getTerm(course_term)
		sb.getInstructor(instructorid)
		sb.getEnrollmentMin(enrollment_min)
		sb.getEnrollmentMax(enrollment_max)
		sb.getEnrollment(enrollment(conn, enrollment_query, courseid, "'" + course_term + "'", sectionid))
		sb.getTime(time)
		sb.getLocation(location)
		s = sb.getItem()

	return s

def prereqs(conn, courseid):
	prereqs = []
	query = select_query + where_clause
	rs = conn.execute(query.format('prerequisites', 'courseid', courseid))

	prerequisites = rs.fetchall()
	for prereq in prerequisites:
		prereqid = prereq[1]
		prereqs.append(prereqid)

	return prereqs

def enrollment(conn, enrollment_query, courseid, term, sectionid):
	enrolled = []
	rs = conn.execute(enrollment_query.format(courseid, term, sectionid))
	enrollment = rs.fetchall()

	for studentid in enrollment:
		enrolled.append(studentid[0])

	return enrolled

def current_term():
	year = datetime.now().year
	month = datetime.now().month
	if month < 7:
		term = "spr"
	else:
		term = "fall"

	return term + str(year)