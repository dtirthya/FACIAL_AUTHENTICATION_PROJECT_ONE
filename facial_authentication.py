#Imported libraries

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Database Configuration

app = Flask(__name__)
app.config['SECRET_KEY'] = '1bc643a3e0afced9c90c4d307b871b678612b1706d2ea0148b54e259ce571ceee4f357863e57b0aacb4e1c0a13e2eb400d05'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Models

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(20), unique=True, nullable=False)

class Images(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=False)
    image = db.Column(db.String(20), nullable=False)

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

if __name__ == '__main__':
    app.run(debug=True)