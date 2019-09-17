#Imported libraries

from flask import render_template
from facial_authentication import app
from facial_authentication.models import User, Images

#Routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/registration')
def registration():
    return render_template('user_registration.html')

@app.route('/login')
def login():
    return render_template('user_login.html')