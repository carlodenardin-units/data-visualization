import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import pearsonr
import matplotlib.font_manager as fm

# CONSTANT: Colors
PRIMARY_TEXT_COLOR = '#0F172A'
SECONDARY_TEXT_COLOR = '#64748B'

# CONSTANT: Font
font_dirs = ["/Users/carlodenardin/Library/Fonts/"]
font_files = fm.findSystemFonts(fontpaths=font_dirs)

for font_file in font_files:
    fm.fontManager.addfont(font_file)

plt.rcParams['font.family'] = 'Segoe UI'

# DATA: Load data
u_data = pd.read_csv("./data.csv")

# DATA: Clean data
u_data.drop('Year', axis = 1, inplace = True)
u_data.drop('Party position', axis = 1, inplace = True)

df = pd.DataFrame()
df["Lab"] = u_data[u_data["Party"] == "Lab"].groupby("Ballot position")["Votes"].sum()
df["Cons"] = u_data[u_data["Party"] == "Cons"].groupby("Ballot position")["Votes"].sum()
df["Lib Dem"] = u_data[u_data["Party"] == "Lib Dem"].groupby("Ballot position")["Votes"].sum()
df["Votes"] = u_data.groupby("Ballot position")["Votes"].sum()
df["Candidates"] = u_data.groupby("Ballot position").count()["Ward code"]
df["Ballot"] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# GRAPH: Settings
fig, ax = plt.subplots(1,2, figsize=(20, 10))

ax[0].tick_params(color = '#1E293B', labelcolor = '#1E293B', labelsize = 14)
ax[1].tick_params(color = '#1E293B', labelcolor = '#1E293B', labelsize = 14)
for spine in ax[0].spines.values():
    spine.set_edgecolor('#1E293B')
for spine in ax[1].spines.values():
    spine.set_edgecolor('#1E293B')

# GRAPH: Settings first plot
ax[0].set(yticklabels=[])
ax[0].get_yaxis().set_ticks([])
ax[0].set(ylabel=None)

ax[0].set_xticks(df["Ballot"])
ax[0].set_xticklabels(df["Ballot"])

ax[0].spines['top'].set_visible(False)
ax[0].spines['left'].set_visible(False)
ax[0].spines['right'].set_visible(False)

fig.subplots_adjust(bottom=0.2)

# GRAPH: Settings second plot
ax[1].set(yticklabels=[])
ax[1].get_yaxis().set_ticks([])
ax[1].set(ylabel=None)

ax[1].set_xticks(df["Ballot"])
ax[1].set_xticklabels(df["Ballot"])

ax[1].spines['top'].set_visible(False)
ax[1].spines['left'].set_visible(False)
ax[1].spines['right'].set_visible(False)

# First plot
ax[0].bar(df["Ballot"], df["Lab"], color = "#fc0352", label="Lab")
ax[0].bar(df["Ballot"], df["Cons"], color = "#4361ee", bottom = df["Lab"], label = "Cons")
ax[0].bar(df["Ballot"], df["Lib Dem"], color = "#ffdd32", bottom = df["Lab"] + df["Cons"], label = "Lib Dem")
sns.lineplot(data=df, x="Ballot", y="Votes", color = "#2a9d8f", linewidth = 1, ax = ax[0], linestyle='-', markers = True, marker = "s", markersize = 8, markerfacecolor = "#2a9d8f", markeredgecolor = "#2a9d8f")

for i, v in enumerate(df["Votes"].div(1000000).round(2)):
    print(i, v)
    ax[0].text(i + 1 - 0.3, v * 1030000, str(v), color='#2a9d8f', fontweight='bold', fontsize = 14)

for dots in ax[0].collections:
    color = dots.get_facecolor()
    dots.set_color(sns.set_hls_values(color, l=0.5))
    dots.set_alpha(1)

ax[0].text(0.5, 1300000, "Votes per Ballot position", color='#2a9d8f', fontweight='bold', fontsize = 18)
ax[0].set_xlabel('Ballot position', fontsize = 16, color = PRIMARY_TEXT_COLOR, labelpad = 15)
ax[0].set(ylim=(0, 1300000))

ax[0].get_legend().remove()

# Second plot
ax[1].bar(df["Ballot"], df["Candidates"], color = "#CBD5E1", bottom = 0)
sns.lineplot(data = df, x = "Ballot", y = "Candidates", color = PRIMARY_TEXT_COLOR, linewidth = 1, ax = ax[1], linestyle='-', markers = True, marker = "s", markersize = 8, markerfacecolor = PRIMARY_TEXT_COLOR, markeredgecolor = PRIMARY_TEXT_COLOR)

for i, v in enumerate(df["Candidates"]):
    print(i, v)
    ax[1].text(i + 1 - 0.25, v + 20, str(v), color=PRIMARY_TEXT_COLOR, fontweight='bold', fontsize = 14)


ax[1].text(0.5, 700, "Candidates per Ballot position", color=PRIMARY_TEXT_COLOR, fontweight='bold', fontsize = 18)
ax[1].set_xlabel('Ballot position', fontsize = 16, color = PRIMARY_TEXT_COLOR, labelpad = 15)
ax[1].set(ylim=(0, 700))

# Bottom source
plt.text(0.12, 0.05, "Source: ", fontsize = 14, transform=plt.gcf().transFigure, weight = "bold", color = PRIMARY_TEXT_COLOR)
plt.text(0.158, 0.05, "https://data.london.gov.uk/dataset/borough-council-election-results-2010", fontsize = 14, transform=plt.gcf().transFigure, weight="ultralight", color = SECONDARY_TEXT_COLOR)

plt.savefig("plot.png", dpi = 300)

# Labour
# Conservative
# Liberal Democrat

