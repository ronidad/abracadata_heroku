
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# df = pd.read_csv("data\combined_data.csv")
# df['Total_deaths'] = df['Death_Illicit_drugs']+df['Death_Opioid']+df['Death_Alchohol']+df['Death_Other_drugs']+df['Death_Amphetamine']
# df = df[['Entity','Year','Total_deaths']]
# df_2015=(df[df['Year']==2015])
# df_2015 = df_2015[['Entity','Total_deaths']]
Gender_depression_df= pd.read_csv('data/Clean_Gender_depression.csv')
data = [Gender_depression_df['%_Depressive_disorders_males'].mean(), Gender_depression_df['%_Depressive_disorders_females'].mean()]
labels = ['Males', 'Females']
#define Seaborn color palette to use
colors = sns.color_palette('pastel')[0:5]
#create pie chart
fig = plt.pie(data, labels = labels, colors = colors, autopct='%.0f%%')
plt.title('Gender Most Affected by Depressive Disorders')
# country = list(df['Entity'])
# deaths = list(df['Total_deaths'])
# print(deaths)
df = px.data.tips()
print(df)
# fig1 = px.bar(df, x="Entity", y="Total_deaths", color="Entity")
#fig = go.Figure(data=[go.histogram(x=country, y=deaths)])
layout = html.Div([
    html.P("Names:"),
    dcc.Dropdown(
        id='names', 
        value='day', 
        options=[{'value': x, 'label': x} 
                 for x in ['smoker', 'day', 'time', 'sex']],
        clearable=False
    ),
    html.P("Values:"),
    dcc.Dropdown(
        id='values', 
        value='total_bill', 
        options=[{'value': x, 'label': x} 
                 for x in ['total_bill', 'tip', 'size']],
        clearable=False
    ),
    dcc.Graph(id="pie-chart"),
])