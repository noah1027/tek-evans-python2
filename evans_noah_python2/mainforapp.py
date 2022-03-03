from flask import Flask, render_template, url_for, redirect, session
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql
from formtest import AddOwner, AddCanine
import cryptography

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Password1!@localhost/Appdata1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'
db = SQLAlchemy(app)
Migrate(app, db)


class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer,primary_key=True)
    dogname = db.Column(db.Text)
    dogage = db.Column(db.Integer)
    breed = db.Column(db.Text)
    gender = db.Column(db.Text)
    owner_id = db.Column(db.Integer)


    def __init__(self, dogname, dogage, breed, gender, owner_id):
        self.dogname = dogname
        self.dogage = dogage
        self.breed = breed
        self.gender = gender
        self.owner_id = owner_id

    def __repr__(self):
        return f"The puppy {self.dogname} is a {self.gender} {self.breed} and is {self.dogage} years old."

class Owner(db.Model):
    __tablename__ = 'owner'
    owner_id = db.Column(db.Integer, primary_key=True)
    ownername = db.Column(db.Text)
    ownerage = db.Column(db.Integer)
    phone = db.Column(db.Text)
    address = db.Column(db.Text)

    def __init__(self, ownername, ownerage, phone, address):
        self.ownername = ownername
        self.ownerage = ownerage
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f"The owner {self.ownername} is {self.ownerage} years old and can be reached at either {self.phone} or {self.address}."


@app.route('/')
def index():
    return render_template('hometest.html')

@app.route('/doglist')
def list_dogs():
    Puppys = Puppy.query.all()
    return render_template('doglist.html', Puppys=Puppys)

@app.route('/ownerlist')
def list_owners():
    Owners = Owner.query.all()
    return render_template('ownerlist.html', Owners=Owners)

@app.route('/dogadd', methods=['GET','POST'])
def add_dog():
    form = AddCanine()

    if form.validate_on_submit():
        dogname = form.dogname.data
        dogage = form.dogage.data
        breed = form.breed.data
        gender = form.gender.data
        owner_id =form.owner_id.data

        new_dog = Puppy(dogname, dogage, breed, gender, owner_id)
        db.session.add(new_dog)
        db.session.commit()

        return redirect(url_for('list_dogs'))

    return render_template('addcanine.html', form=form)

@app.route('/owneradd', methods=['GET', 'POST'])
def add_owner():
    form = AddOwner()

    if form.validate_on_submit():
        ownername = form.ownername.data
        ownerage = form.ownerage.data
        phone = form.phone.data
        address = form.address.data

        new_owner = Owner(ownername, ownerage, phone, address)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_owners'))
    return render_template('addowner.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)