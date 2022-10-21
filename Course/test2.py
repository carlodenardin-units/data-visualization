
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

pd.options.plotting.backend = "plotly"

np.random.seed(4); cols = list('abc')
X = np.random.randn(50,len(cols))
df=pd.DataFrame(X, columns=cols)
df.iloc[0]=0
fig = df.plot()

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Random datastream"),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,
        n_intervals=0
    ),
    dcc.Graph(id='graph'),
])

@app.callback(
    Output('graph', 'figure'),
    [Input('interval-component', "n_intervals")]
)

def streamFig(value):
    global df
    Y = np.random.randn(1,len(cols))
    df2 = pd.DataFrame(Y, columns = cols)
    df = df.append(df2, ignore_index=True)
    df.tail()
    df3=df.copy()
    df3 = df3.cumsum()
    fig = df3.plot()
    return(fig)

app.run_server()