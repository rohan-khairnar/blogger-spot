# This file will use once to create database and there table at innitial.

from models.meta import dbconnect, dbcreate
from models.databases import metadata

try:
    dbcreate()
    eng = dbconnect()
    metadata.create_all(eng)
    print ("database created successfully")
except:
    print ("Database already exist")