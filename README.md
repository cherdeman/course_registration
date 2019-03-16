# REGIE Course Registration System
This project is an implementation of the REGIE course registration system, completed as the final project for Object Oriented Programming. The goal of the project is to implement a functional course registration system, with a particular focus on using object oriented design and principals. This implementation focuses on system interaction by student users, so has less developed capabilities for other potential user types (like instructors, etc.)

## Getting Started
The following instructions will help you get a copy of this project up and running on your own computer. 

### Prerequisites
This system is developed in Python 3.6. If you do not have Python 3.6 installed, you can download it [here](https://www.python.org/downloads/).

The database system used in this project is MySQL Community Server version 8.0.15. The most recent version of the MySQL Community server can be downloaded [here](https://dev.mysql.com/downloads/).

A virtual environment is recommended for managing package dependencies required for this project. I used [pyenv](https://github.com/pyenv/pyenv#installation) but feel free to deviate.

### Cloning the repository
Clone the repository to the desired location using `git clone https://github.com/cherdeman/course_registration.git` or `git clone git@github.com:cherdeman/course_registration.git` if you have ssh credentials enabled on your github account.

### Installing requirements
To install the necessary package dependencies for this project, run the command `pip3 -r install requirements.txt` from the root of this repository. Note that the primary dependencies are SQLAlchemy and mysqlclient to facilitate the interaction between Python and the MySQL backend, and pytest to run the testing infrastructure. Tabulate is used to "prettify" printed output.

### Database configuration
Once MySql is installed on your computer, you can access is from the command line with the command `mysql -u root -p`. The system requires a database called "regie" and a user called "user". To create the database and user on your system, run the following series of commands from the command line:

```
mysql -u root -p        # Enter the MySQL command line interface as the root user
CREATE DATABASE regie; # Create a database named regie
USE regie;            # Use the regie database
CREATE USER 'user'@'localhost'; # Create a user called "user" with no password
GRANT ALL PRIVILEGES ON regie.* TO 'user'@'localhost'; # Grant all privileges on the regie database to user
exit # Exit the MySQL CLI
```
To populate the database from its initial state, run the command `python3 database/generate_data_tables.py` from the root of this repository. You can now interact with the live tables using the MySQL CLI or the database GUI of your choice.

### Running tests
The suite of tests can be run using the command `pytest` from the root of this repository. 

## Interacting with the system
This system was not developed with a front end, so all interaction with the system takes place from the command line. To interact with the system, run the command `python3 login.py` from the root of the repository. Note that this command must be run AFTER `python3 database/generate_data_tables.py`. You can login as any username/password combination found in the "student" table in the database. I suggest starting with the username "cstudent" and password "temp". Follow the prompts from there. Note the the only valid courseid's currently available in the system (for adding/dropping a course) are 1100, 1200, and 2100.

## Acknowledgements
Thank you to Professor Mark Shacklette and TA's Terry Lynch and John Hadidian-Baugher for their support and assistance in developing this project!
