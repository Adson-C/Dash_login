import dash
import dash_bootstrap_components as dbc
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
import os
from flask import Flask

server = Flask(__name__)

app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.QUARTZ])
server = app.server