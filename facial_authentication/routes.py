#Imported libraries

from flask import render_template, redirect, url_for, flash
from facial_authentication import app, db
from facial_authentication.forms import RegistrationForm, LoginForm
from facial_authentication.models import User
from werkzeug.utils import secure_filename
import os

#Routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        #Making a name of the user for creating a folder
        u_folder_name = str.upper(form.first_name.data) + '_' + str.upper(form.middle_name.data) + '_' + str.upper(form.last_name.data)
        #Getting the path of the  current working directory
        original_path = os.getcwd()
        #Navigating to the static folder
        os.chdir(os.getcwd() + '\\facial_authentication\\static')
        #Creating a folder in the name of the user inside the static directory
        os.mkdir(u_folder_name)
        #Getting the details of the image uploaded
        filename = secure_filename(form.image.data.filename)
        #Setting the name of the file
        ren_name = u_folder_name + '_' + 'REGISTRATION'
        #Renaming the file
        filename = ren_name
        #Setting current working directory to the previously created folder of the user
        os.chdir(os.getcwd() + '\\' + u_folder_name)
        #Saving the image to that folder
        form.image.data.save(filename)
        #Saving the current path to a variable to use for database
        image_path = os.getcwd() + '\\'
        #Reverting back to the original path
        os.chdir(original_path)
        image = url_for(image_path, filename=form.image.data.filename)
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