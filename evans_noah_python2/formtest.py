from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, IntegerField
from wtforms.validators import DataRequired

class AddCanine(FlaskForm):
    dogname = StringField("What's your dog's name?", validators=[DataRequired()])
    dogage = IntegerField("How old is your dog?", validators=[DataRequired()])
    breed = StringField("What breed is your dog?", validators=[DataRequired()])
    gender = StringField("What gender is your dog?", validators=[DataRequired()])
    owner_id =IntegerField('What is your owner id?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddOwner(FlaskForm):
    ownername = StringField("What is your name?", validators=[DataRequired()])
    ownerage = IntegerField("What is your age?", validators=[DataRequired()])
    phone = StringField("What is your phone number?", validators=[DataRequired()])
    address = StringField("What is your address?", validators=[DataRequired()])
    submit = SubmitField('Submit')
