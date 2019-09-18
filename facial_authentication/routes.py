#Imported libraries

from flask import render_template, redirect, url_for, flash, request
from facial_authentication import app, db
from facial_authentication.forms import RegistrationForm, LoginForm
from facial_authentication.models import User, Images
import os

#Routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        u_folder_name = str.upper(form.first_name.data) + ' ' + str.upper(form.middle_name.data) + ' ' + str.upper(form.last_name.data)
        original_path = os.getcwd()
        os.chdir(original_path + '\\facial_authentication\\static')
        os.mkdir(u_folder_name)
        os.chdir(os.getcwd() + '\\' + u_folder_name + '\\')
        for file in request.files.getlist(form.image.data):
            file.save(os.getcwd(), file)
        os.chdir(original_path)
        path = 'C:\\Users\\Tirthya Dasgupta\\Documents\\PROJECTS\PYTHON_PROJECTS\\FLASK_MACHINE_LEARNING PROJECTS\\FACIAL_AUTHENTICATION_PROJECT_ONE\\facial_authentication\\static' + '\\' + u_folder_name + '\\'
        os.path.join(path, form.image.data)
        image = url_for('static', filename=path)
        user = User(first_name=form.first_name.data, middle_name=form.middle_name.data, last_name=form.last_name.data, email=form.email.data, u_image=image)
        db.session.add(user)
        db.session.commit()
        flash({form.first_name.data}, 'YOUR ACCOUNT HAS BEEN CREATED!')
        return redirect(url_for('home'))
    return render_template('user_registration.html', title='REGISTER', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('user_login.html', title='LOGIN', form=form)