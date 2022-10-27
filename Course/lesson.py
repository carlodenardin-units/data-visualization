import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

df = pd.read_csv('gapminder.csv')

fig = px.scatter(
    df,
    x = 'Income',
    y = 'Life expectancy',
    color = 'Region'
)

print(fig)