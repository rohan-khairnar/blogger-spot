"""
This view file deals with API for blog related operations.
It contains view, add, edit & delete blog related API's.
consideration:
    status: 0 = success, status: 1 = failed.
"""

from flask import Flask, render_template, request,redirect, url_for 
from sqlalchemy.sql import select
from models.meta import dbconnect
from models.databases import blogs, users
from app import app

# This will create an engine for database operations
eng = dbconnect()

# It will render home.html file along with all blogs & their related user data
@app.route('/')
def homePage():
    con = eng.connect()
    result = con.execute(select([blogs, users]).select_from(blogs.join(users)))
    blogs_data = result.fetchall()
    blogs_data.reverse()
    return render_template('home.html', blogs_data = blogs_data)

# It will render singleblog.html page. 
@app.route('/blog')
def newBlogPage():
    return render_template('singleblog.html',type='add')

# Save new blog and return to home.html
@app.route('/add-blog', methods=['POST'])
def addBlog():
    try:
        con = eng.connect()
        data = request.form
        con.execute(blogs.insert(),[data])
        return redirect(url_for("homePage"))
    except:
        return {"status":1}

# Render to singleblog.html along with blog data
# It takes blogid as input
@app.route('/<blogid>', methods=['GET'])
def editBlogPage(blogid):
    try:
        con = eng.connect()
        result = con.execute(select([blogs.c.userid,blogs.c.blogtitle,blogs.c.blogdescription]).where(blogs.c.blogid == blogid))
        blog_data = result.fetchone()
        return render_template('singleblog.html',blog_data=blog_data,type='edit', blogid=blogid)
    except:
        return {"status":1}

# Save updated blogs
@app.route('/update', methods=['PUT'])
def updateBlog():
    try:
        data = request.form
        con = eng.connect()
        result = con.execute(blogs.update().where(blogs.c.blogid==data['blogid']).values(data))
    
        return {"status":0}
    except:
        return {"status":1}

# Delete blog. Takes blogid as input.
@app.route('/delete/<int:blogid>', methods=['DELETE'])
def deleteBlog(blogid):
    try:
        con = eng.connect()
        result = con.execute(blogs.delete().where(blogs.c.blogid==blogid))
        return {"status":0}
    except:
        return {"status":1}

