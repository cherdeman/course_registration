#This file creates the user table and loads the user_data.csv data into the table

from db_connect import connect

# Define queries
drop = "DROP TABLE IF EXISTS {} CASCADE;"

create_users = """CREATE TABLE IF NOT EXISTS users (
	firstname   text    NOT NULL,
	lastname	text	NOT NULL,
	id			int  	NOT NULL,
	attributes  JSON	NOT NULL,
	PRIMARY KEY(id) 
);"""

load_users = """INSERT INTO users (firstname, lastname, id, attributes) 
				VALUES ("admin", "admin",  0, '{}'), 
					   ("Claire", "Herdeman", 1, '{}'),
					   ("A", "Professor", 2, '{}');
			 """

load_users_infile = """LOAD DATA LOCAL INFILE '../data/user_data.csv' 
				INTO TABLE users
				COLUMNS TERMINATED BY ','
				OPTIONALLY ENCLOSED BY '"'
				ESCAPED BY '"'
				LINES TERMINATED BY '\n'
				IGNORE 1 LINES;"""

# Establish db connection
conn = connect()

# Execute queriess
conn.execute(drop.format('users'))
conn.execute(create_users)
conn.execute(load_users)