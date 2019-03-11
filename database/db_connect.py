# Database connection untility file

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

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