# This file will helps to create tables under database.

# This module contains the sqlalchemy expression based table definitions.
# They will be converted to real sql statements and tables will be subsequently created by create_all function in initdb.py.

from sqlalchemy import (
    Table,
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    ForeignKey,
    UnicodeText
    )
from sqlalchemy import MetaData
import datetime

#metadata is the module that converts Python code into real sql statements, specially for creating tables.
metadata = MetaData()

users = Table('users',metadata,
        Column('userid',Integer, primary_key=True),
        Column('username',Text,nullable=False),
        Column('userpassword',UnicodeText,nullable=False)
)

blogs = Table('blogs',metadata,
        Column('blogid', Integer, primary_key=True),
        Column('userid', Integer, ForeignKey('users.userid'), primary_key=True ),
        Column('blogtitle',Text,nullable=False),
        Column('blogdescription', UnicodeText, nullable=False),
        Column('entrydate',DateTime,nullable=False, default=datetime.datetime.now().date())
)

