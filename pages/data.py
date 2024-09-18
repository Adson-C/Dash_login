from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import *

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash_bootstrap_templates import load_figure_template

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user
from dash.exceptions import PreventUpdate

load_figure_template(["quartz"])
card_style = {
    'width': '800px',
    'min-height': '300px',
    'padding-top': '25px',
    'padding-right': '25px',
    'padding-left': '25px',
}

df = pd.DataFrame(np.random.randn(100, 1), columns=["data"])
fig = px.line(df, x=df.index, y="data", template="quartz")


# =========  Layout  =========== #
def render_layout(username):
    template = dbc.Card([
                dcc.Location(id="data-url"),
                html.Legend("Olá, {}!".format(username)),
                dcc.Graph(figure=fig),

                html.Div([
                    dbc.Button("Logout", id="logout_button"),
                ], style={"padding": "20px", "justify-content": "end", "display": "flex"})

            ], style=card_style, className="align-self-center")
    return template