# This file will helps to create tables under database.

# This module contains the sqlalchemy expression based table definitions.
# They will be converted to real sql statements and tables will be subsequently created by create_all function in initdb.py.

from sqlalchemy import (
    Table,
    Column,
    Index,
    Integer,
    Text,
    UnicodeText
    )
from sqlalchemy import MetaData

#metadata is the module that converts Python code into real sql statements, specially for creating tables.
metadata = MetaData()

"""
Create products table. 
contains all products for sales.
prodcode = products code. unique for each product.
prodrate = products rate.
prodname = products name.
proddesc = products description.
"""
products = Table('products',metadata,
        Column('prodcode',Integer, primary_key=True),
        Column('prodrate',Integer,nullable=False),
        Column('prodname',UnicodeText,nullable=False),
        Column('proddesc',Text)
)