# defined function to create database at innitial
# defined function to create engine for database operations

import sqlalchemy as sa
import os

# It will create database at innitial.
def dbcreate():
    url = os.environ.get('DB_URL')
    eng = sa.create_engine(url, echo=False)
    conn = eng.connect()
    conn.execute("commit")
    conn.execute("create database blogger")
    conn.close()
    return (url+'/blogger')

# create database engine.
def dbconnect():
    url = os.environ.get('DB_URL')+"/blogger" 
    engine = sa.create_engine(url, echo=False)
    return engine