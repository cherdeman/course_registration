# This document containts unit tests for the database connection

import pytest
import  database.db_connect as db
import sqlalchemy as sa
#import MySQLdb

def test_url():
	dburl = db.URL(
            "mysql",
            host="localhost",
            username="user",
            database="regie",
            port=3306,
        )
	dburl == "mysql://user@localhost:3306/regie"


