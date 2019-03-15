from database.db_connect import connect
import startup_functions as s

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
					WHERE
				   """

def main():
	conn = s.connect()
	students = s.make_students()
	print("made students {}".format(students.keys()))
	instructors = s.make_instructors(conn, select_query.format('instructor'))
	print("made instructors {}".format(instructors.keys()))
	courses = s.make_courses()
	print("made courses {}".format(courses.keys()))

if __name__ == "__main__":
	main()

