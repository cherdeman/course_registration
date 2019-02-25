#This file creates the user table and loads the user_data.csv data into the table

from db_connect import connect

# General Queries
drop = "DROP TABLE IF EXISTS {} CASCADE;"

# User table queries
create_users = """CREATE TABLE IF NOT EXISTS users (
	firstname   varchar(20)    NOT NULL,
	lastname	varchar(20)	   NOT NULL,
	id			int  		   NOT NULL,
	type  		varchar(20)	   NOT NULL,
	PRIMARY KEY(id) 
);"""

load_users = """INSERT INTO users (firstname, lastname, id, type) 
				VALUES ("admin", "admin",  0, 'admin'), 
					   ("Claire", "Herdeman", 1, 'student'),
					   ("A", "Professor", 2, 'instructor');
			 """

load_users_infile = """LOAD DATA LOCAL INFILE '../data/user_data.csv' 
				INTO TABLE users
				COLUMNS TERMINATED BY ','
				OPTIONALLY ENCLOSED BY '"'
				ESCAPED BY '"'
				LINES TERMINATED BY '\n'
				IGNORE 1 LINES;"""

# Course table queries
create_courses = """CREATE TABLE IF NOT EXISTS courses (
					id			varchar(10)		NOT NULL,
					title		varchar(50) 	NOT NULL,
					dept  		varchar(20) 	NOT NULL,
					enrollment_limit int        NOT NULL,
					PRIMARY KEY(id) 
				);"""

load_courses = """INSERT INTO courses (id, title, dept, enrollment_limit) 
				  VALUES ("10100", "Object Oriented Programming",  "CS", 30);
			   """

# Establish db connection
conn = connect()

# Execute queries
conn.execute(drop.format('users'))
conn.execute(create_users)
conn.execute(load_users)

conn.execute(drop.format('courses'))
conn.execute(create_courses)
conn.execute(load_courses)
