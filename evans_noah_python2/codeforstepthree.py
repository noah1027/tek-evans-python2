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
from codeforsteptwo import ownerframe, puppyframe



"""
Please note, before you run this page, please go to 'codeforsteptwo.py' and place '#' in front of 
the ownerframe.to_sql and puppyframe.to_sql commands. For some reason, when this page is ran,
it will try to re-upload the records from the codeforsteptwo.py page (likely because of the import
statement above).
"""






print("---------------------------------------------------------------")
print("count of records for each column in the owner dataframe:")
print(ownerframe.count())
print("---------------------------------------------------------------")
print("count of records for each column in the puppy dataframe:")
print(puppyframe.count())

def columncount(dataframe):
    column = []
    for i in dataframe:
        column.append(i)
    print(column.__len__())
print("---------------------------------------------------------------")
print("The number of columns in the owner dataframe:")
columncount(ownerframe)
print("---------------------------------------------------------------")
print("The number of columns in the puppy dataframe:")
columncount(puppyframe)

print("---------------------------------------------------------------")
print("The count of dogs in the puppy dataframe by gender:")
genderdogs = puppyframe.groupby('gender')[['gender']]
print(genderdogs.count())
#Note, for the owner dataframe, there is no common values between observations that could be grouped by
#to fix this, I will join the two tables and do count of puppy's for each owner
print("---------------------------------------------------------------")
print("Total quantity of dogs owned by owner:")
mergedframe = pd.merge(ownerframe,puppyframe,how='left',on='owner_id')
countdogsbyowner = mergedframe.groupby('ownername')[['ownername']]
print(countdogsbyowner.count())
