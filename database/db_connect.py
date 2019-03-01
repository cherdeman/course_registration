# Database connection untility file

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

def connect():
        dburl = URL(
            "mysql",
            host="localhost",
            username="cherdeman",
            database="reggie",
            port=3306,
        )
        return create_engine(dburl)

conn = connect()

def update(conn, table, col, val, where_field, where_val):
	update = "UPDATE {} SET {} = {} WHERE {} = {}".format(table, col, val, where_field, where_val)
	conn.execute(update)