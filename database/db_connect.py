# Database connection untility file

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from tabulate import tabulate

def connect():
        dburl = URL(
            "mysql",
            host="localhost",
            username="user",
            database="regie",
            port=3306,
        )
        return create_engine(dburl)

conn = connect()

def update(conn, table, col, val, where_field, where_val):
    update = "UPDATE {} SET {} = {} WHERE {} = {}".format(table, col, val, where_field, where_val)
    conn.execute(update)


def add(conn, table, cols, values):
    add = "INSERT INTO {} {} VALUES {};".format(table, cols, values)
    print(add   )
    conn.execute(add)

def delete(conn, table, where_col, where_val):
    delete = "DELETE FROM {} WHERE {} = {}".format(table, where_col, where_val)
    conn.execute(delete)

def view_courses(conn, course_input):
    course_view = """SELECT c.courseid, d.department, c.title, c.description
                    FROM course c
                    JOIN department d
                    USING(dept_code)
                    WHERE courseid in ({})""".format(course_input)
    rs = conn.execute(course_view)
    rows = rs.fetchall()

    headers = ["Course Number", "Department", "Course Title", "Description"]
    printable = []
    for row in rows:
        cnum = row[0]
        dept = row[1]
        title = row[2]
        description = row[3]
        printable.append([cnum, dept, title, description])

    print(tabulate(printable, headers))

