from flask import Flask,session,redirect,url_for,escape,request
app=Flask(__name__)
app.secret_key='any random string'
@app.route('/')
def index():
   if 'username' in session:
      username = session['username']
            return 'Logged in as ' + username + '<br>' + \
      "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + \
    "click here to log in</b></a>"