# flask_wtf - registration form etc
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login Up')

    
    


# FlaskForm - registration form , login form 
# wtforms StringField class, for string field like username or email
# from wtforms.validators import DataRequired - Validators
# Length validator - set min and max character for Username
# Password Field for password
# EqualTo - Tocheck if Confirm password is same as password
# SubmitField - for Submit Button
# BooleanField - for remember me - true of false
# Secret Key for cross site attack Modifying cookies