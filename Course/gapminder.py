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
    df.query('Year>=2000'),
    x = 'Income',
    y = 'Life expectancy',
    color = 'Region',
    size = 'Population',
    size_max = 60,
    log_x = True,
    hover_name = 'Country',
    hover_data = {c: False for c in df.columns},
    color_discrete_map = color_dict,
    animation_frame = 'Year',
    animation_group = 'Country',
)

fig.update_layout(
    plot_bgcolor = 'white',
    title = 'Gapminder<br><sup>Data from gapminder.org, CC-BY license</sup>',
    font = dict(color = 'dimgray'),
    legend = dict(
        itemsizing='trace'
    ),
)
fig.update_xaxes(showline = True, linecolor = 'dimgrey', gridcolor = 'lightgrey', linewidth = 1, showspikes = True, spikecolor = 'dimgray', spikethickness = 1)
fig.update_yaxes(showline = True, linecolor = 'dimgrey', gridcolor = 'lightgrey', linewidth = 1, showspikes = True, spikecolor = 'dimgray', spikethickness = 1)
fig.update_traces(marker = dict(opacity = 0.9, line = dict(width = 1, color = 'dimgrey')))

fig.show()