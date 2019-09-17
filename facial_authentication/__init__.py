#Imported Libraries

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Database Configuration

app = Flask(__name__)
app.config['SECRET_KEY'] = '1bc643a3e0afced9c90c4d307b871b678612b1706d2ea0148b54e259ce571ceee4f357863e57b0aacb4e1c0a13e2eb400d05'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Tirthya Dasgupta\\Documents\\PROJECTS\\PYTHON_PROJECTS\\FLASK_MACHINE_LEARNING PROJECTS\\FACIAL_AUTHENTICATION_PROJECT_ONE\\user_database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


#Importing Routes
from facial_authentication import routes
