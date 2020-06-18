# File will help to serve project on web server.
from flask import Flask
app = Flask(__name__)

# import all API's from views.user and views.blog
from views.user import *
from views.blog import *

if __name__ == '__main__':
    app.run(debug=True)
