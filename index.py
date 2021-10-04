import dash
from dash import dcc
from dash import html
import plotly.express as px


from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# from app import app, server
from app import app, server
from apps import app1, app2, app3, app4

#server = app.server


# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        
        html.P(
            "Drug abuse in Africa", className=""
        ),
        dbc.Nav(
            [
                dbc.NavLink("Deaths", href="/", active="exact"),
                #dbc.NavLink("Gender", href="/apps/app2", active="exact"),
                dbc.NavLink("Time series", href="/apps/app3", active="exact"),
                dbc.NavLink("Countries", href="/apps/app4", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return app1.layout
    elif pathname == "/apps/app2":
        return app2.layout
    elif pathname == "/apps/app3":
        return app3.layout
    elif pathname == "/apps/app4":
        return app4.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )



if __name__ == '__main__':
    app.run_server(debug=True)