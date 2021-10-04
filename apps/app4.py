
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

from app import app

# df = px.data.gapminder()
df = pd.read_csv("data/combined_data.csv")
df['Total_deaths'] = df['Death_Illicit_drugs']+df['Death_Opioid']+df['Death_Alchohol']+df['Death_Other_drugs']+df['Death_Amphetamine']
df = df[['Entity','Year','Total_deaths']]
#df = df.sort_values()[0]
#df = df.sort_values(by="Year")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

layout = html.Div([
        html.H2("Death due to drug abuse over time", style={'text-align': 'center'}),

    dcc.Dropdown(id='dpdn2', value=['Kenya', 'Uganda'], multi=True,
                 options=[{'label': x, 'value': x} for x in
                          df['Entity'].unique()]),
                        dcc.Graph(id="bar-chart"),
      
      
])

@app.callback(
    Output("bar-chart", "figure"), 
    [Input("dpdn2", "value")])


def update_line_chart(country_chosen):
    mask = df.Entity.isin(country_chosen)
    print(mask)
    
    fig = px.bar(df[mask],
              x="Year",
              y="Total_deaths",  
              color="Entity")
    #fig.update_xaxes(type='category')
    return fig