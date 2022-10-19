# Library
import matplotlib.pyplot as plt
import matplotlib.colors as mc
import pandas as pd
import seaborn as sns

# Scale the label size
sns.set(font_scale=0.70)

# CONSTANT: Colors
TEXT_COLOR = "#0F172A"
SUBTEXT_COLOR = "#475569"
GRID_COLOR = "#F1F5F9"
HEATMAP_COLOR_MAP = ['#FEEDDE','#FDD0A2','#FDAE6B','#FD8D3C','#E6550D','#A63603']
LINEPLOT_COLOR_MAP = ['#1B9E77', '#666666','#7570B3','#E7298A','#66A61E','#E6AB02','#A6761D','#D95f02']

# CONSTANT: Steps
STEPS = [0, 0.1, 0.2, 0.4, 0.6, 1]

def cleanData(df):
    print("Debug: cleaning data frame process")
    df['Age group'] = df['Age group'].str[:-2]
    xLabels = df['Age group']
    df.drop(['Age group'], axis=1, inplace=True)
    df.rename(index=xLabels, inplace=True)
    return df

def generateColorMap():
    print("Debug: generating color map process")
    cdict = {'red': (), 'green': (), 'blue': ()}
    for step, color in zip(STEPS, HEATMAP_COLOR_MAP):
        rgb = mc.hex2color(color)
        cdict['red'] = cdict['red'] + ((step, rgb[0], rgb[0]),)
        cdict['green'] = cdict['green'] + ((step, rgb[1], rgb[1]),)
        cdict['blue'] = cdict['blue'] + ((step, rgb[2], rgb[2]),)
    return cdict

def setupHeatMapPlot(ax):
    ax.set_facecolor(GRID_COLOR)
    ax.annotate(
        'Birth cohort:',
        xy = (1, 1),
        xytext=(0, 10),
        fontsize = 8,
        weight='heavy',
        color = SUBTEXT_COLOR
    )
    ax.annotate(
        'group of people born during a particular period',
        xy=(1, 1), 
        xytext=(1.35, 10),
        fontsize = 8,
        weight='normal',
        color = SUBTEXT_COLOR
    )
    ax.annotate(
        '% Obesity',
        xy = (1, 1),
        xytext=(9.5, 4.6),
        fontsize = 10,
        weight='normal',
        rotation = 270,
        color = TEXT_COLOR
    )
    plt.xticks(rotation = 0)
    plt.title(
        "Obesity study (1971-2006) from early childhood through adulthood across birth cohorts",
        fontsize=8,
        color = SUBTEXT_COLOR,
        fontweight = "light",
        loc="left"
    )
    plt.suptitle(
        "Birth cohort vs Age group Obesity Prevalence",
        fontsize=11,
        color = TEXT_COLOR,
        fontweight="normal",
        x=0.402,
        y=0.955
    )
    plt.xlabel('Age group', fontsize = 10, color = TEXT_COLOR, labelpad=10)
    plt.ylabel('Birth cohort', fontsize = 10, color = TEXT_COLOR, labelpad=10)
    plt.tight_layout()

def setupLinePlot(ax):
    ax.grid(False)
    ax.set_facecolor('white')
    ax.yaxis.grid(color = '#E2E8F0')

    ax.annotate(
        'Birth cohort:',
        xy = (1, 1),
        xytext=(0.6, 0.5),
        fontsize = 8,
        weight='heavy',
        color = SUBTEXT_COLOR
    )
    ax.annotate(
        'group of people born during a particular period',
        xy=(1, 1), 
        xytext=(1.35, 10),
        fontsize = 8,
        weight='normal',
        color = SUBTEXT_COLOR
    )
        
    plt.xticks(rotation = 0)
    plt.title(
        "Obesity study (1971-2006) from early childhood through adulthood across birth cohorts",
        fontsize=8,
        color = SUBTEXT_COLOR,
        fontweight = "light",
        loc="left"
    )
    plt.suptitle(
        "Age trends in obesity prevalence by birth cohort",
        fontsize=11,
        color = TEXT_COLOR,
        fontweight="normal",
        x=0.352,
        y=0.955
    )
    plt.xlabel('Age group', fontsize = 10, color = TEXT_COLOR, labelpad=10)
    plt.ylabel('% Obesity', fontsize = 10, color = TEXT_COLOR, labelpad=10)
    plt.tight_layout()

    legend = plt.legend(bbox_to_anchor=(0.82, 0.4), loc='upper left', borderaxespad=0)
    frame = legend.get_frame()
    frame.set_facecolor(GRID_COLOR)
    frame.set_edgecolor(GRID_COLOR)
    


if __name__ == "__main__":
    print("Debug: generating heatmap process")
    # Import
    df = pd.read_csv('./data.csv')

    # Clean process
    df = cleanData(df)

    # Generate color map
    cdict = generateColorMap()
    colorMap = mc.LinearSegmentedColormap('test', cdict)

    # Generate heatmap plot
    ax1 = sns.heatmap(df.T, cmap = colorMap, linewidths=1, linecolor='white')

    # Beautify plot
    setupHeatMapPlot(ax1)

    # Save plot
    plt.savefig('heatmap.png', dpi = 1200)

    # Clean plot
    plt.close()

    # Generate lineplot
    ax2 = sns.lineplot(data = df, markers=True, markersize=9, palette = LINEPLOT_COLOR_MAP, dashes = False)
    
    # Beautify plot
    setupLinePlot(ax2)

    plt.savefig('scatterplot.png', dpi = 1200)