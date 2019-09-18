#Imported Libraries

from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError

#Forms

class RegistrationForm(FlaskForm):
    first_name = StringField('FIRST NAME', validators=[DataRequired()])
    middle_name = StringField('MIDDLE NAME')
    last_name = StringField('LAST NAME', validators=[DataRequired()])
    email = StringField('EMAIL', validators=[DataRequired(), Email()])
    image = FileField('IMAGE', validators=[DataRequired()])
    submit = SubmitField('SIGN UP')

class LoginForm(FlaskForm):
    email = StringField('EMAIL', validators=[DataRequired(), Email()])
    image = FileField('IMAGE', validators=[DataRequired()])
    submit = SubmitField('LOGIN')




