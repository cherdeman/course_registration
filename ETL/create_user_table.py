#This file creates the user table and loads the user_data.csv data into the table

from db_connect import connect, execute_query



drop = "DROP TABLE IF EXISTS {} CASCADE;"

create_users = """CREATE TABLE IF NOT EXISTS users (
	username	text	NOT NULL,
	id			int  	NOT NULL,
	attributes  JSON	NOT NULL,
	PRIMARY KEY(id) 
);"""

load_users = """INSERT INTO users (username, id, attributes) 
				VALUES ('admin', 000000, '{}'), 
					   ('cherdeman', 000001, '{}'),
					   ('aprofessor', 000002, '{}');
			 """

load_users_infile = """LOAD DATA LOCAL INFILE '../data/user_data.csv' 
				INTO TABLE users
				COLUMNS TERMINATED BY ','
				OPTIONALLY ENCLOSED BY '"'
				ESCAPED BY '"'
				LINES TERMINATED BY '\n'
				IGNORE 1 LINES;"""

conn = connect()

conn.execute(drop.format('users'))
conn.execute(create_users)
conn.execute(load_users)