from db_connect import connect
from classes.person_classes import Student

# Sample query and obhect creation using SQLAlchemy
student_query = """
				SELECT * 
				FROM users
				WHERE type = 'student'
				"""

conn = connect()

results = conn.execute(student_query)

all_students = results.fetchall()

for student in all_students:
	student[student[2]] = Student(student[0], student[1])