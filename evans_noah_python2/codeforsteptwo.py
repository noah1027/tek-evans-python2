import sqlalchemy
from flask import Flask, render_template, url_for, redirect, session
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql
from formtest import AddOwner, AddCanine
from mainforapp import db, Puppy, Owner
import pandas as pd
import numpy as np



#I used https://www.youtube.com/watch?v=lNL4sCa3otU for assistance with migrating data from DF to MySQL, also used DF documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
engine = sqlalchemy.create_engine('mysql+pymysql://root:Password1!@localhost/Appdata1')
ownerframe = pd.read_csv(r'C:\Users\tveva\PycharmProjects\tek-evans-python2\evans_noah_python2\csvs for step two\ownertable.csv', index_col=False)
puppyframe = pd.read_csv(r'C:\Users\tveva\PycharmProjects\tek-evans-python2\evans_noah_python2\csvs for step two\puppytable.csv', index_col=False)
print(ownerframe)
print(puppyframe)
ownerframe.to_sql('owner', engine, schema='appdata1', if_exists='append', index=False)
puppyframe.to_sql('puppies', engine, schema='appdata1', if_exists='append', index=False)