from sqlalchemy import Table, create_engine
from sqlalchemy.sql import select
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import warnings
import os

conn = sqlite3.connect('data.sqlite')
engine = create_engine('sqlite:///data.sqlite')

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

users_table = Table('users', Users.metadata)

def create_users_table():
    Users.metadata.create_all(engine)

create_users_table()
# verificar tabela com pandas

# import pandas as pd
# c= conn.cursor()
# df = pd.read_sql("SELECT * FROM users", conn)
# df