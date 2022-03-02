from flask import Flask, render_template, url_for, redirect, session
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql
from formtest import AddOwner, AddCanine
from mainforapp import db, Puppy, Owner



db.session.add(my_puppy)
db.session.commit()