import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px 
import pandas as pd

df = pd.read_csv("data\combined_data.csv")
df['Total_deaths'] = df['Death_Illicit_drugs']+df['Death_Opioid']+df['Death_Alchohol']+df['Death_Other_drugs']+df['Death_Amphetamine']
dff = df[['Entity','Year','Total_deaths']]

#df = px.data.gapminder()
all_countries = df.Entity.unique()
df.head()
app = dash.Dash(__name__)

app.layout = html.Div([
    
    dcc.Dropdown(id='dpdn2', value=['Kenya'], multi=True,
                 options=[{'label': x, 'value': x} for x in
                          df['Entity'].unique()]),
                        dcc.Graph(id="line-chart"),
    
    
      
])

@app.callback(
    Output("line-chart", "figure"), 
    [Input("dpdn2", "value")])


def update_line_chart(country_chosen):
    mask = df.Entity.isin(country_chosen)
    fig = px.line(df[mask], 
        x="Year", y="Total_deaths")
    return fig

app.run_server(debug=True)