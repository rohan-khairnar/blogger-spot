# defined function to create database at innitial
# defined function to create engine for database operations

import sqlalchemy as sa
import os

# It will create database at innitial.
def dbcreate():
    uri = "postgres://postgres:pass@localhost"
    eng = sa.create_engine(uri, echo=False)
    conn = eng.connect()
    conn.execute("commit")
    conn.execute("create database blogger")
    conn.close()
    return (uri+'/blogger')

# create database engine.
def dbconnect():
    uri = "postgres://postgres:pass@localhost/blogger" 
    engine = sa.create_engine(uri, echo=False)
    return engine