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
    register = dbc.Card([
                 html.Legend("Cadastra-se"),
                dbc.Input(id="user_register", placeholder="Username", type="text"),
                dbc.Input(id="pwd_register", placeholder="Password", type="password"),
                dbc.Input(id="email_register", placeholder="email", type="email"),
                dbc.Button("Registrar", id="register_btn"),
                html.Span("", style={"text=align": "center"}),
                html.Div([
                    html.Label("Ou", style={"margin-right": "5px"}),
                    dcc.Link("faça Login", href="/login"),
                ], style={"padding-top": "20px", "justify-content": "center", "display": "flex"})

    ], style=card_style)
    return register