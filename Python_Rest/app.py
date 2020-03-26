from flask import Flask, escape, url_for
from datetime import datetime
import re

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
def hello():
    return 'Hello, Vinay'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/hello/<name>',)
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"
    
     
    

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

@app.route('/login')
def login():
    return 'login'

if __name__ == '__main__':
    app.run()

