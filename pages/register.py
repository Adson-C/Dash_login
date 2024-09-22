from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import numpy as np
import plotly.express as px

from app import *

from dash.exceptions import PreventUpdate
from werkzeug.security import generate_password_hash
import re

card_style = {
    'width': '300px',
    'min-height': '300px',
    'padding-top': '25px',
    'padding-right': '25px',
    'padding-left': '25px',
    'align-self': 'center'
}

def render_layout(message):
    message = "Ocorreu algum erro durente o registro." if message == "error" else message
    register = dbc.Card([
                 html.Legend("Cadastra-se"),
                dbc.Input(id="user_register", placeholder="Username", type="text"),
                dbc.Input(id="pwd_register", placeholder="Password", type="password"),
                dbc.Input(id="email_register", placeholder="email", type="email"),
                dbc.Button("Registrar", id="register_btn"),
                html.Span(message, style={"text=align": "center"}),
                html.Div([
                    html.Label("Ou", style={"margin-right": "5px"}),
                    dcc.Link("faça Login", href="/login"),
                ], style={"padding-top": "20px", "justify-content": "center", "display": "flex"})

    ], style=card_style)
    return register

# callback de registro
@app.callback(
    Output("register-state", "data"),
    Input("register_btn", "n_clicks"),
    
    [State("user_register", "value"), State("pwd_register", "value"), State("email_register", "value")],)

def register(n_clicks, username, password, email):
    if n_clicks is None:
        raise PreventUpdate
    
    if username is not None and password is not None and email is not None:
        hashed_password = generate_password_hash(password, method='sha256')
        ins = users_table.insert().values(username=username, password=hashed_password, email=email)
        conn= engine.connect()
        conn.execute(ins)
        # conn.commit()
        conn.close()
        return ''
    else:
        return 'Deu erro'