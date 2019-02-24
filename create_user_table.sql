/*
This file creates the user table and loads the user_data.csv data into the table
*/


DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE IF NOT EXISTS users (
	username	text	NOT NULL,
	id			int  	NOT NULL,
	attributes  JSON	NOT NULL,
	PRIMARY KEY(id) 
);

LOAD DATA LOCAL INFILE '../data/user_data.csv' INTO TABLE users;