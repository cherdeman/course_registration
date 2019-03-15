# Class implementing course search functionality
import database.db_connect as db
from tabulate import tabulate
from sqlalchemy import text
from startup_functions import current_term

class Search():
	# __instance = None

	# def getInstance():
	# 	if Search._instance == None:
	# 		Search()
	# 	return Search.__instance

	def __init__(self):
		self.conn = db.connect()
	# 	if Search.__instance != None:
	# 		return Search.__instance
	# 	else:
	# 		Search.__instance = self
		
	def control(self):
		search = True
		while search:
			where_clause = self._option()
			query = self._generate_query(where_clause)
			self._search(query)
			cont = input("Would you like to search again? (y/n): ")	
			if cont == "n":
				search = False

	def _search(self, query):
		rs = self.conn.execute(text(query))
		results = rs.fetchall()
		
		headers = ["Course ID Num", "Department", "Title", "Description", "Offered this term?", "Spots Available"]
		printable = []
		for result in results:
			num = result[1]
			dept = result[2]
			title = result[3]
			desc = result[4]
			offered = result[5]
			spots = result[6]
			printable.append([num, dept, title, desc, offered, spots])

		print(tabulate(printable, headers))

	def _generate_query(self, where_clause):
		base = """
		SELECT DISTINCT c.courseid,  
			   d.department, 
			   c.title, 
			   c.description, 
			   CONCAT(i.firstname, " ", i.lastname) AS instructor_name,
			   CASE WHEN s.enrollment_max IS NULL THEN "No"
			   		WHEN s.enrollment_max IS NOT NULL THEN "Yes" END AS offered_this_term,
			   CASE WHEN e.enrollment IS NULL THEN s.enrollment_max 
			        ELSE s.enrollment_max - e.enrollment END AS spots_available
		FROM course c
		JOIN department d
		USING(dept_code)
		LEFT JOIN `section` s
		USING(courseid)
		JOIN instructor i
		USING(instructorid)
		LEFT JOIN (
			SELECT courseid, term, count(*) as enrollment
			FROM grades
			GROUP BY courseid, term
		) e 
		USING(courseid, term) 
		WHERE term = '{}'
		""".format(current_term())

		query = base + where_clause

		return query

	def _option(self):
		option_dict = {
			1: ["course id number", int],
			2: ["department", str],
			3: ["title", str],
			4: ["description", str],
			5: ["instructor name", str]
		}
		print("What field would you like to search by?")
		for i in range(1, 6):
			print("{}) {}".format(i, option_dict[i][0]))

		option = int(input("Please enter the number of the field you'd like to select: "))
		term = input("Please enter your search term: ")

		if option_dict[option][1] == int:
			where = "AND courseid = {}".format(int(term))
		else:
			if option == 5:
				field = "CONCAT(i.firstname, ' ', i.lastname)"
			else:
				field = option_dict[option][0]
			where = "AND {0} LIKE '%{1}%';".format(field, term)

		return where
