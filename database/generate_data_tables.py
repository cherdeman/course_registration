#This file creates the user table and loads the user_data.csv data into the table

from db_connect import connect

# General Queries
drop = "DROP TABLE IF EXISTS {} CASCADE;"
create = "CREATE TABLE IF NOT EXISTS {} ({});"
load = "INSERT INTO {} {} VALUES {};"

def generate_table(name, fields, cols, data):
	conn.execute(drop.format(name))
	conn.execute(create.format(name, fields))
	conn.execute(load.format(name, cols, data))

# Establish db connection
conn = connect()

# student table queries
student_name = 'student'
student_fields = """studentid   int            NOT NULL,
				   firstname   varchar(20)    NOT NULL,
				   lastname	   varchar(20)	   NOT NULL,
				   username    varchar(21),
				   password    varchar(20),
			       PRIMARY KEY(studentid)
			     """
student_cols = '(studentid, firstname, lastname, password)'
student_data = """(100001, "CS", "Student", "temp"), 
				  (100002, "Policy", "Student", "temp")"""

generate_table(student_name, student_fields, student_cols, student_data)

# instructor table queries
instructor_name = 'instructor'
instructor_fields = """instructorid   int            NOT NULL,
							firstname      varchar(20)    NOT NULL,
							lastname	   varchar(20)	  NOT NULL,
							dept_code      int            NOT NULL,
							username    varchar(21),
				   			password    varchar(20),
							PRIMARY KEY(instructorid)
					"""
instructor_cols = '(instructorid, firstname, lastname, dept_code, password)'
instructor_data = """(200001, "A", "Professor", 1, "temp"),
					 (200002, "Gary", "Becker", 2, "temp")
				  """
generate_table(instructor_name, instructor_fields, instructor_cols, instructor_data)

# department table queries
dept_name = "department"
dept_fields = """dept_code	int 		NOT NULL,
				 department  varchar(20) NOT NULL,
				 PRIMARY KEY (dept_code)
			  """
dept_cols = '(dept_code, department)' 
dept_data = """(1, "Computer Science"),
			   (2, "Public Policy")
			"""

generate_table(dept_name, dept_fields, dept_cols, dept_data)

# Course table queries
course_name = 'course'
course_fields = """courseid    int 		 NOT NULL,
				   dept_code   int 		 NOT NULL,
				   title       varchar(50) NOT NULL,
				   description text,
				   PRIMARY KEY (courseid)
				"""
course_cols = '(courseid, dept_code, title, description)'
course_data = """(1100, 1, "Intro to Programming", "Learn basic programming!"),
				 (1200, 1, "Object Oriented Programming", "Learn about patterns!"),
				 (2100, 2, "Analytical Politics I", "Learn about... analyzing politics?")
			  """

generate_table(course_name, course_fields, course_cols, course_data)

# section queries
section_name = 'section'
section_fields = """sectionid int NOT NULL,
					courseid  int NOT NULL,
					term      varchar(20) NOT NULL,
					instructorid int NOT NULL,
					enrollment_min int NOT NULL,
					enrollment_max int NOT NULL,
					time timestamp,
					location varchar(5),
					enrollment int,
					PRIMARY KEY (sectionid, courseid, term)
				 """
section_cols = '(sectionid, courseid, term, instructorid, enrollment_min, enrollment_max)'
section_data = """(10, 1100, "fall2018", 200001, 5, 10),
				  (10, 1200, "fall2018", 200001, 5, 10),
				  (10, 2100, "fall2018", 200002, 5, 10),
				  (10, 1100, "spr2019", 200001, 5, 10),
				  (10, 1200, "spr2019", 200001, 5, 10),
				  (10, 2100, "spr2019", 200002, 5, 10)
			   """

generate_table(section_name, section_fields, section_cols, section_data)

# pre-reqs
pre_name = 'prerequisites'
pre_fields = """courseid int NOT NULL,
				prereqid int NOT NULL
			 """
pre_cols = '(courseid, prereqid)'
pre_data = '(1200, 1100)'

generate_table(pre_name, pre_fields, pre_cols, pre_data)

# Grades/enrollment
grade_name = 'grades'
grade_fields = """studentid int 		NOT NULL,
				  courseid  int 		NOT NULL,
				  sectionid int 		NOT NULL,
				  term      varchar(20) NOT NULL,
				  grade     varchar(2),
				  PRIMARY KEY (studentid, courseid, term)
			   """
grade_cols = '(studentid, courseid, sectionid, term, grade)'
grade_data = """(100001, 1100, 10, "fall2018", 'A'),
				(100001, 2100, 10, "fall2018", 'B+'),
				(100002, 1100, 10, "fall2018", 'B'),
				(100002, 2100, 10, "fall2018", 'A-'),
				(100002, 2100, 10, "spr2019", NULL)
			 """

generate_table(grade_name, grade_fields, grade_cols, grade_data)

