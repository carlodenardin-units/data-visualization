###########
# Library #
###########

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import seaborn as sns
import matplotlib.font_manager as fm

###########################
# Constant: Colors, Fonts #
###########################
PRIMARY_TEXT_COLOR = '#0F172A'
SECONDARY_TEXT_COLOR = '#64748B'

font_dirs = ["/Users/carlodenardin/Library/Fonts/"]
font_files = fm.findSystemFonts(fontpaths=font_dirs)

for font_file in font_files:
    fm.fontManager.addfont(font_file)

plt.rcParams['font.family'] = 'Segoe UI'

####################
# Custom functions #
####################
def roundValue(value):
    t = str(round(value / 1000000, 2))
    if len(t) == 3:
        t += "0"
    return t

##########
# Import #
##########
u_data = pd.read_csv("./data.csv")

##################
# Data: Cleaning #
##################
u_data.drop('Year', axis = 1, inplace = True)
u_data.drop('Party position', axis = 1, inplace = True)

###################
# Data: Structure #
###################
df = pd.DataFrame()
df["Lab"] = u_data[u_data["Party"] == "Lab"].groupby("Ballot position")["Votes"].sum()
df["Cons"] = u_data[u_data["Party"] == "Cons"].groupby("Ballot position")["Votes"].sum()
df["Lib Dem"] = u_data[u_data["Party"] == "Lib Dem"].groupby("Ballot position")["Votes"].sum()
df["Votes"] = u_data.groupby("Ballot position")["Votes"].sum()
df["Candidates"] = u_data.groupby("Ballot position").count()["Ward code"]
df["Ballot"] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

####################
# Figure: Settings #
####################

# Create grid
fig, ax = plt.subplot_mosaic(
    [
        ['left', 'info'],
        ['left', 'lower right'],
    ],
    figsize = (20, 10),
    layout = "constrained",
    gridspec_kw = {'width_ratios': [1, 0.6]}
)

# Adjust the bottom padding
fig.subplots_adjust(bottom = 0.2)

###########################
# Plot 1: Ballot vs Votes #
###########################

ax['left'].bar(
    df["Ballot"],
    df["Lab"],
    color = "#fc0352",
    label = "Lab"
)

ax['left'].bar(
    df["Ballot"],
    df["Cons"],
    color = "#4361ee",
    bottom = df["Lab"],
    label = "Cons"
)

ax['left'].bar(
    df["Ballot"],
    df["Lib Dem"],
    color = "#ffc300",
    bottom = df["Lab"] + df["Cons"],
    label = "Lib Dem"
)

sns.lineplot(
    data=df, 
    x="Ballot", 
    y="Votes", 
    color = SECONDARY_TEXT_COLOR, 
    ax = ax['left'], 
    linestyle='-', 
    markers = True, 
    marker = "s", 
    markersize = 8, 
    markerfacecolor = PRIMARY_TEXT_COLOR, 
    markeredgecolor = PRIMARY_TEXT_COLOR
)

####################
# Plot 1: Settings #
####################

# Remove the unnecessary axes
ax['left'].spines['left'].set_visible(False)
ax['left'].spines['top'].set_visible(False)
ax['left'].spines['right'].set_visible(False)

# Setting the x axis values and ticks
ax['left'].tick_params(
    color = PRIMARY_TEXT_COLOR,
    labelcolor = PRIMARY_TEXT_COLOR,
    labelsize = 16
)
ax['left'].set_xticks(df["Ballot"])

# Remove the y axis
ax['left'].set(ylabel=None)
ax['left'].set(yticklabels = [])
ax['left'].set_yticks([])

# Title
ax['left'].text(
    0.51,
    1280000,
    "Votes per Ballot position",
    color=PRIMARY_TEXT_COLOR,
    fontweight='bold',
    fontsize = 20
)

# Subtitle
ax['left'].text(
    0.53,
    1220000,
    "Number of votes (in milions) for different Ballot positions of 3 parties",
    color = SECONDARY_TEXT_COLOR,
    fontweight = 'normal',
    fontsize = 17
)

# Setting the x axis label
ax['left'].set_xlabel(
    'Ballot position', 
    fontsize = 18, 
    color = PRIMARY_TEXT_COLOR, 
    labelpad = 15
)

ax['left'].legend(
    loc = 'upper center',
    bbox_to_anchor = (0.5, -0.12),
    fancybox = True,
    shadow = True,
    ncol = 3,
    fontsize = 14
)

# Add values on the plot
for i, v in enumerate(df["Votes"].div(1000000).round(2)):
    ax['left'].text(
        i + 1 - 0.23,
        v * 1030000,
        str(v),
        color = PRIMARY_TEXT_COLOR, 
        fontweight = 'bold',
        fontsize = 14
    )

for i, v in enumerate(df["Lab"]):
    t = roundValue(v)
    ax['left'].text(
        i + 1 - 0.21,
        v - 70000,
        str(t[0:4]),
        color = "white",
        fontweight = 'normal',
        fontsize = 14
    )

for (i, v), j in zip(enumerate(df["Lab"] + df["Cons"]), df["Cons"]):
    t = roundValue(j)
    ax['left'].text(
        i + 1 - 0.21,
        v - 70000,
        str(t[0:4]),
        color = "white",
        fontweight = 'normal',
        fontsize = 14
    )

for (i, v), j in zip(enumerate(df["Lab"] + df["Cons"] + df["Lib Dem"]), df["Lib Dem"]):
    t = roundValue(j)
    ax['left'].text(
        i + 1 - 0.21,
        v - 70000,
        str(t[0:4]),
        color = "white",
        fontweight = 'normal',
        fontsize = 14
    )


################################
# Plot 2: Ballot vs Candidates #
################################

ax['lower right'].bar(
    df["Ballot"],
    df["Candidates"],
    color = "#CBD5E1",
    bottom = 0
)

sns.lineplot(
    data = df,
    x = "Ballot",
    y = "Candidates",
    color = SECONDARY_TEXT_COLOR,
    linewidth = 1,
    ax = ax['lower right'],
    linestyle='-',
    markers = True,
    marker = "s",
    markersize = 8,
    markerfacecolor = PRIMARY_TEXT_COLOR,
    markeredgecolor = PRIMARY_TEXT_COLOR
)

####################
# Plot 2: Settings #
####################

# Remove the unnecessary axes
ax['lower right'].spines['left'].set_visible(False)
ax['lower right'].spines['top'].set_visible(False)
ax['lower right'].spines['right'].set_visible(False)

# Setting the x axis values and ticks
ax['lower right'].tick_params(
    color = '#1E293B',
    labelcolor = '#1E293B',
    labelsize = 16
)
ax['lower right'].set_xticks(df["Ballot"])

# Remove the y axis
ax['lower right'].set(ylabel=None)
ax['lower right'].set(yticklabels = [])
ax['lower right'].set_yticks([])

# Title
ax['lower right'].text(
    0.55,
    840,
    "Candidates per Ballot position",
    color = PRIMARY_TEXT_COLOR,
    fontweight = 'bold',
    fontsize = 20
)

# Sub title
ax['lower right'].text(
    0.55,
    770,
    "Number of candidates for different Ballot positions of 3 parties",
    color = SECONDARY_TEXT_COLOR,
    fontweight = 'normal',
    fontsize = 17
)

# Setting the x axis label
ax['lower right'].set_xlabel(
    'Ballot position',
    fontsize = 18,
    color = PRIMARY_TEXT_COLOR,
    labelpad = 15
)

# Add values on the plot
for i, v in enumerate(df["Candidates"]):
    ax['lower right'].text(
        i + 1 - 0.30,
        v + 40,
        str(v),
        color=PRIMARY_TEXT_COLOR,
        fontweight='bold',
        fontsize = 14
    )

#########################
# Information on screen #
#########################

# Remove the unnecessary axes
ax['info'].spines['left'].set_visible(False)
ax['info'].spines['top'].set_visible(False)
ax['info'].spines['right'].set_visible(False)
ax['info'].spines['bottom'].set_visible(False)

# Remove the y axis
ax['info'].set(ylabel=None)
ax['info'].set(yticklabels = [])
ax['info'].set_yticks([])

# Remove the x axis
ax['info'].set(xlabel = None)
ax['info'].set(xticklabels = [])
ax['info'].set_xticks([])

# Ballot position explanation
ax['info'].text(
    -0.31,
    1.105,
    "Ballot position: ",
    color = SECONDARY_TEXT_COLOR,
    fontweight = 'bold',
    fontsize = 16,
    va = "baseline",
    ha = "left",
    multialignment = "left"
)

ax['info'].text(
    0.005,
    1.105,
    "alphabetical position of candidates' surnames",
    color = SECONDARY_TEXT_COLOR,
    fontweight = 'normal',
    fontsize = 17,
    va = "baseline",
    ha = "left",
    multialignment = "left"
)

# Trend explanation
ax['info'].text(
    -0.31,
    0.6,
    "There is a decreasing trend starting from the \n7th ballot position due to the fact that there \nare fewer candidates for all three parties.",
    color = SECONDARY_TEXT_COLOR,
    fontweight = 'normal',
    fontsize = 18,
    va = "baseline",
    ha = "left",
    multialignment = "left"
)

# Line for the trend explanation
fig.add_artist(
    lines.Line2D(
        [0.47, 0.54],
        [0.70, 0.78],
        color = SECONDARY_TEXT_COLOR,
        alpha = 0.3
    )
)

#################################
# Other stuff and save the plot #
#################################

plt.text(
    0.145,
    0.02,
    "Data source: ",
    fontsize = 18,
    transform = plt.gcf().transFigure,
    weight = "bold",
    color = PRIMARY_TEXT_COLOR
)

plt.text(
    0.222,
    0.02,
    "https://data.london.gov.uk/dataset/borough-council-election-results-2010",
    fontsize = 18,
    transform = plt.gcf().transFigure,
    weight = "ultralight",
    color = SECONDARY_TEXT_COLOR
)

plt.savefig("plot.png", dpi = 400)
