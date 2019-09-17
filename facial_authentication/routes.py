#Imported libraries

from flask import render_template, redirect, url_for, flash
from facial_authentication import app, db
from facial_authentication.forms import RegistrationForm, LoginForm
from facial_authentication.models import User, Images

#Routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data, middle_name=form.middle_name.data, last_name=form.last_name.data, email=form.email.data, u_image=form.image.data)
        db.session.add(user)
        db.session.commit()
        flash({form.first_name.data}, 'YOUR ACCOUNT HAS BEEN CREATED!')
        return redirect(url_for('home'))
    return render_template('user_registration.html', title='REGISTER', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('user_login.html', title='LOGIN', form=form)