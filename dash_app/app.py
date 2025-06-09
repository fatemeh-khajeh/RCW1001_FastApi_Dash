

import dash
from dash import html, dcc


# initializer 'application Dash
app = dash.Dash(__name__, requests_pathname_prefix ='/dashboard/')


# Definir Dash layout avec 4 graph
app.layout = html.Div(children=[
    html.Div([
        html.A('Acceuil', href='/'),
        "|",
        html.A("Logout", href="/logout")
    ], style={'marginTop':25}),
    
    html.H1(children = "Example de Dashboard" ),
    
    html.H2("*** Bar Graph *** "),
    dcc.Graph(
        id="exm1",
        figure={
            "data":[
                {"x":[5,7,12], "y":[10,16,11] , "type":"bar" , "name":"exmple1"},
                {"x":[8,18,22], "y":[5,8,3] , "type":"bar" , "name":"exmple2"}
            ]
        }
    ),
    
    html.H2("*** Line Graph *** "),
    dcc.Graph(
        id="exm2",
        figure={
            "data":[
                {"x":[1,3,5], "y":[10,12,14] , "type":"line" , "name":"exmple3"},
                {"x":[2,4,6], "y":[13,15,17] , "type":"line" , "name":"exmple4"}
            ]
        }
    ),
    
    html.H2("*** scatter Plot Graph *** "),
    dcc.Graph(
        id="exm3",
        figure={
            "data":[
                {"x":[1,3,5,7], "y":[10,12,14,16] , "type":"scatter" , "mode":"markers","name":"scatter exmpl1"},
                {"x":[2,4,6,8], "y":[13,15,17,19] , "type":"scatter" , "mode":"markers","name":"scatter exmpl2"}
            ]
        }
    ),
    
    html.H2("*** Pie Chart Graph *** "),
    dcc.Graph(
        id="exm4",
        figure={
            "data":[
                {"labels":["A","B","C"], "y":[10,12,14] , "type":"pie" , "name":"pie chart expl1"},
            ],
            "layout":{"title":"pie chart example"}
        }
    ),
    
    
    
])

server = app.server

