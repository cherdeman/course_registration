from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.pool import QueuePool

def connect(poolclass=QueuePool):
        dburl = URL(
            "mysql",
            host="localhost",
            username="cherdeman",
            database="reggie",
            port=3306,
        )
        return create_engine(dburl, poolclass=poolclass)

conn = connect()

def execute_query(query, columns=None, verbose=False):
    if verbose:
        print("Query is ", query)
    query = """SET ROLE {}; {};""".format(role, query)
    return pd.read_sql(query, conn)