import pandas as pd
import plotly.graph_objs as go
import plotly.express as px


##########
# Import #
##########
df = pd.read_csv('gapminder.csv', sep = ',')
df_info = pd.read_csv('gapminder-info.csv', sep = ',', index_col = 0)

##########
# Colors #
##########
color_dict = {
    'Asia': '#ff798e',
    'Europe': '#ffeb33',
    'Africa': '#33dded',
    'Americas': '#98ef33',
}

# Smaller year will be first and then smaller Population will be first
df = df.sort_values(['Year', 'Population'], ascending = [True, False])

# Bubble chart
fig = px.scatter(
    df.query('Year==2020'),
    x = 'Income',
    y = 'Life expectancy',
    color = 'Region',
    size = 'Population',
    size_max = 60,
    log_x = True,
    hover_name = 'Country',
    hover_data = {c: False for c in df.columns},
    color_discrete_map = color_dict,
)

fig.update_layout(
    plot_bgcolor = 'white',
)

fig.update_xaxes(showline = True, linecolor = 'dimgrey', gridcolor = 'lightgrey', linewidth = 1)
fig.update_yaxes(showline = True, linecolor = 'dimgrey', gridcolor = 'lightgrey', linewidth = 1)



fig.update_xaxes(
    title = 'Income'
)

fig.show()