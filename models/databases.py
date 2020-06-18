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

# This schema is for users table.
# userid : primary key, autoincreament and foreign key in blogs table.
# firstname : mindatory , lastname : optional
# loginid : login will based on this field.
# userpassword : contains password require for login.
users = Table('users',metadata,
        Column('userid',Integer, primary_key=True),
        Column('firstname',Text,nullable=False),
        Column('lastname',Text),
        Column('loginid',Text,nullable=False, unique=True),
        Column('userpassword',UnicodeText,nullable=False, unique=True)
)

# This schema is for blogs table.
# blogid : primary key, autoincreament.
# userid : foreign key taken from users table.
# blogtitle : mindatory. It will contain title of blog.
# blogdescription : It will contain description of blog.
# entrydate : It will add automaticaly at the time of adding blog or updating blog.
blogs = Table('blogs',metadata,
        Column('blogid', Integer, primary_key=True),
        Column('userid', Integer, ForeignKey('users.userid') ),
        Column('blogtitle',Text,nullable=False),
        Column('blogdescription', UnicodeText, nullable=False),
        Column('entrydate',DateTime,nullable=False, default=datetime.datetime.now().date())
)

