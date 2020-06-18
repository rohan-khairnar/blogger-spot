"""
This file is written for user related operation.
It contains register new user, login user API's. 
Consideration :
status: 0 = success, status: 1 = failed.
"""


from flask import Flask, render_template, request,redirect, url_for 
from sqlalchemy.sql import select
from models.meta import dbconnect
from models.databases import users
from app import app

# create engine for database operations
eng = dbconnect()

# Return login page
@app.route('/login')
def loginPage():
    return render_template('login.html')

# Login User API
# status 3 : loginId not exist in database.
# status 2 : loginId exist but wrong password.
# status 1 : API operation get failed.
# status 0 : loggedIn success.
# Return user data.
@app.route('/user-login', methods=['POST'])
def login():
    try:
        con = eng.connect()
        data = request.form
        result = con.execute(select([users.c.userid,users.c.loginid,users.c.firstname,users.c.lastname,users.c.userpassword]).where(users.c.loginid == data['loginid']))
        result = result.fetchone()
        if result == None:
            return {"status":3}
        else:
            if (data['userpassword']==result['userpassword']):
                return {"status":0,"firstname":result['firstname'],"lastname":result['lastname'],"userid":result['userid'],"loginid":result['loginid']}
            else:
                print("wrong pass")
                return {"status":2}
    except:
        return {"status":1}

# Register new user.
@app.route('/user-register', methods=['POST'])
def register():
    try:
        con = eng.connect()
        data = request.form
        con.execute(users.insert(),[data])
        return {"status":0}
    except:
        return {"status":1}
