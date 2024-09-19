from dash import html, dcc
import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

from app import *

from pages import login, register, data


app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
           dcc.Location(id='base-url', refresh=False),
           
           dcc.Store(id='login-state', data=''),
           dcc.Store(id='register-state', data=''),
            
            html.Div(id='page-content', style={'height': '100vh', 'display': 'flex', 'justifyContent': 'center'}),
        ]),
    ])
], fluid=True)


@app.callback(Output('base-url', 'pathname'),
              [

                Input('login-state', 'data'),
                Input('register-state', 'data'),
              ])
def render_page_contente(login_state, register_state):
    ctx = dash.callback_context
    if ctx.triggered:
        # [{'prop_id': 'register-state.data', 'value': 'error'}]
        trigg_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if trigg_id == 'login-state' and login_state == 'sucess':
            return '/data'
        if trigg_id == 'login-state' and login_state == 'error':
            return '/login'

        if trigg_id == 'register-state':
            if register_state == '':
                return '/login'
            else:
                return '/register'

@app.callback(Output('page-content', 'children'),
              Input('base-url', 'pathname'),
              [State('login-state', 'data'), State('register-state', 'data'),])
def render_page_content(pathname, login_state, register_state):
    if pathname == '/login' or pathname == '/':
        return login.render_layout()

    if pathname == '/register':
        return register.render_layout(register_state)

    if pathname == '/data':
        return data.render_layout("Adson")

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)