#Imported Libraries

from facial_authentication import db

#Models

class User(db.Model):
    u_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    u_image = db.Column(db.String(20), unique=True, nullable=False)
    is_authenticated = db.Column(db.Boolean, default=False)

class Images(db.Model):
    i_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.u_id'), nullable=False, primary_key=False)
    uploaded_image = db.Column(db.String(20), nullable=False)