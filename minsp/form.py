from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, FloatField, DateField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError

class LoginForm(FlaskForm):
    id = IntegerField('cpr_number', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')

class SignUpForm(FlaskForm):
    cpr_number = IntegerField('cpr_number', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('password', validators=[DataRequired()])
    address = StringField('address')

class InsertResultForm(FlaskForm):
    result = FloatField('result', validators=[DataRequired()])
    date_of_test = DateField('date_of_test', validators=[DataRequired()])