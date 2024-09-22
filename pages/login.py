from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import numpy as np
np.bool_ = np.bool_
# import plotly.express as px
from werkzeug.security import check_password_hash
from flask_login import login_user
from dash.exceptions import PreventUpdate

from app import *

card_style = {
    'width': '300px',
    'min-height': '300px',
    'padding-top': '25px',
    'padding-right': '25px',
    'padding-left': '25px',
    'align-self': 'center'
}

def render_layout(message):
    message = "Ocorreu algum erro durente o login." if message == "error" else message
    login = dbc.Card([
                html.Legend("Login"),
                dbc.Input(id="user_login", placeholder="Username", type="text"),
                dbc.Input(id="pwd_login", placeholder="Password", type="password"),
                dbc.Button("Login", id="login_btn"),
                html.Span(message, style={"text=align": "center"}),
                html.Div([
                    html.Label("Ou", style={"margin-right": "5px"}),
                    dcc.Link("Cadastre-se", href="/register"),
                ], style={"padding-top": "20px", "justify-content": "center", "display": "flex"})                 
        ], style=card_style)
    return login

@app.callback(
    Output("login-state", "data"),
    Input("login_btn", "n_clicks"),
    
    [State("user_login", "value"), 
    State("pwd_login", "value")],)
def successful_login(n_clicks, username, password):
    if n_clicks == None:
        raise PreventUpdate

    # Verifica se o usuário existe no banco de dados
    user = Users.query.filter_by(username=username).first()

    # Verifica se o usuário existe e se a senha foi fornecida
    if user and password:
        # Compara a senha fornecida com a senha armazenada no banco de dados
        if check_password_hash(user.password, password):
            login_user(user)
            return 'sucess'
        else:
            return 'error'
    else:
        return 'error'

# def successful_login(n_clicks, username, password):
#     if n_clicks == None:
#         raise PreventUpdate

#     # Verifica se o usuário existe no banco de dados
#     user = Users.query.filter_by(username=username).first()

#     # Verifica se o usuário existe e se a senha foi fornecida
#     if user and password:
#         # Compara a senha fornecida com a senha armazenada no banco de dados
#         if check_password_hash(user.password, password):
#             login_user(user)
#             return 'success'
#         else:
#             return 'error'
#     else:
#         return 'error'

# def sucessful_login(n_clicks, username, password):
#     if n_clicks == None:
#         raise PreventUpdate

#     user = Users.query.filter_by(username=username).first()

#     if user and password is not None:
#         if check_password_hash(user.password, password):
#             login_user(user)
#             return 'sucess'
#         else:
#             return 'error'
#     else:
#         return 'error'