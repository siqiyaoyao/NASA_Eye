import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px


colorscales = px.colors.named_colorscales()
df = px.data.iris()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Color Scale"),
    dcc.Dropdown(
        id='colorscale', 
        options=[{"value": x, "label": x} 
                 for x in colorscales],
        value='viridis'
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    [Input("colorscale", "value")])
def change_colorscale(scale):
    fig = px.scatter(
        df, x="sepal_width", y="sepal_length", 
        color="sepal_length", color_continuous_scale=scale)
    return fig

app.run_server(debug=True)