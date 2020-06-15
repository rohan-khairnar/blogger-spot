# defined function to create database at innitial
# defined function to create engine for database operations

import sqlalchemy as sa
import os

def dbcreate():
    uri = "mysql+pymysql://%s:%s@%s" % (os.environ.get('DB_USERNAME'),os.environ.get('DB_PASSWORD'), os.environ.get('DB_HOST'))
    eng = sa.create_engine(uri, echo=False)
    conn = eng.connect()
    conn.execute("commit")
    conn.execute("create database sadguru")
    conn.close()
    return (uri+'/sadguru')

def dbconnect():
    uri = "mysql+pymysql://%s:%s@%s/sadguru" % (os.environ.get('DB_USERNAME'),os.environ.get('DB_PASSWORD'), os.environ.get('DB_HOST'))
    engine = sa.create_engine(uri, echo=False)
    return engine