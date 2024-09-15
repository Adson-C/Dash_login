from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import numpy as np
import plotly.express as px

from app import *

card_style = {
    'width': '300px',
    'min-height': '300px',
    'padding-top': '25px',
    'padding-right': '25px',
    'padding-left': '25px',
    'align-self': 'center'
}

def render_layout():
    login = dbc.Card([
                 html.Legend("Login"),
                dbc.Input(id="user_login", placeholder="Username", type="text"),
                dbc.Input(id="pwd_login", placeholder="Password", type="password"),
                dbc.Button("Login", id="login_btn"),
                html.Span("", style={"text=align": "center"}),
                html.Div([
                    html.Label("Ou", style={"margin-right": "5px"}),
                    dcc.Link("Cadastre-se", href="/register"),
                ], style={"padding-top": "20px", "justify-content": "center", "display": "flex"})

                 
    ], style=card_style)
    return login