from database.db_connect import connect
from classes.course_classes import Course, Section
from classes.course_builder import CourseBuilder, SectionBuilder
from utils.functions import current_term

# Define queries
select_query = """
				SELECT * 
				FROM {} 
				"""

where_clause = """
				WHERE {} = {}
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

def make_course(courseid):
	conn = connect()
	query = select_query + where_clause
	rs = conn.execute(query.format('course', 'courseid', courseid))
	course = rs.fetchone()

	if course is not None:
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
	else:
		c = None
	
	return c

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
