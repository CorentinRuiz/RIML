import dash
from dash import dcc, html
import plotly.graph_objs as go
import json
import sys

app = dash.Dash(__name__)

if(len(sys.argv) != 2):
    print("Usage: python script.py nom_projet")
    sys.exit(1)

nom_du_projet = sys.argv[1]

json_file_path = f'./metrics/{nom_du_projet.split("/")[1]}--metrics.json'

with open(json_file_path, "r") as json_file:
    data = json.load(json_file)

communication_rate_map = data["communication_rate_map"]
services = list(communication_rate_map.keys())
communication_rates = list(communication_rate_map.values())

topics_diversity = data["topics_diversity"]
labels = ["Producers", "Consumers", "Services"]
values = [data["producers_number"], data["consumers_number"], data["services_number"]]


# Création du layout du tableau de bord
app.layout = html.Div(children=[
    html.H1(f"Metrics dashboard of {nom_du_projet}", style={'text-align': 'center', 'color': 'black'}),
    
    html.Div([
        html.Div([
            html.H4("Number of producers", style={'color': 'white'}),
            html.Div(data["producers_number"], style={'font-size': '36px', 'font-weight': 'bold', 'color': 'white'}),
        ], style={'background-color': '#34495e', 'padding': '20px', 'border-radius': '10px', 'text-align': 'center'}),
        html.Div([
            html.H4("Number of consumers", style={'color': 'white'}),
            html.Div(data["consumers_number"], style={'font-size': '36px', 'font-weight': 'bold', 'color': 'white'}),
        ], style={'background-color': '#34495e', 'padding': '20px', 'border-radius': '10px', 'text-align': 'center'}),
        html.Div([
            html.H4("Number of services", style={'color': 'white'}),
            html.Div(data["services_number"], style={'font-size': '36px', 'font-weight': 'bold', 'color': 'white'}),
        ], style={'background-color': '#34495e', 'padding': '20px', 'border-radius': '10px', 'text-align': 'center'}),
        html.Div([
            html.H4("Number of topics", style={'color': 'white'}),
            html.Div(data["topics_number"], style={'font-size': '36px', 'font-weight': 'bold', 'color': 'white'}),
        ], style={'background-color': '#34495e', 'padding': '20px', 'border-radius': '10px', 'text-align': 'center'}),
    ], style={'display': 'flex', 'justify-content': 'space-evenly', 'align-items': 'center'}),
    
    dcc.Graph(
        id='Consumer-Producer-Services-pie',
        figure={
            'data': [
                go.Pie(labels=labels, values=values, hole=0.4)
            ],
            'layout': go.Layout(
                title='Ratio of Producers, Consumers and Services',
            )
        }
    ),
    dcc.Graph(
        id='communication-rate-bar',
        figure={
            'data': [
                go.Bar(x=services, y=communication_rates)
            ],
            'layout': go.Layout(
                title='Communication Rates for Services',
                xaxis=dict(title='Services'),
                yaxis=dict(title='Communication Rates')
            )
        }
    ),

    html.H2("Topics diversity"),

    html.Div([
        html.P(round(topics_diversity*10)/10, style={'margin-left': '40px', 'font-size': '50px', 'font-weight': 'bold'}),
        html.P("topic(s)", style={'position': 'relative', 'top': '30px', 'left': '10px', 'font-size': '25px'}),
        html.Hr(style={'height': '200px', 'background': 'white', 'position': 'relative', 'top': '5px', 'left': '-40px', 'transform': 'rotate(65deg)'}),
        html.Div([
            'for',
            html.Div(data['services_number'], style={'font-size': '45px', 'margin': '0 10px'}),
            "service(s)"], style={'left': '-70px', 'top': '40px', 'position': 'relative', 'display': 'flex', 'align-items': 'center', 'font-size': '15px'}),
    ], style={'width': '300px', 'display': 'flex', 'justify-content': 'center', 'background': 'rgb(52, 73, 94)', 'color': 'white', 'border-radius': '10px'}),
])

if __name__ == '__main__':
    app.run_server(debug=True)
