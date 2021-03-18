#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
#import sys, getopt
df = pd.read_csv('Foreign_Exchange_Rates.csv',
                 usecols=[1,7], names=['DATE', 'CAD_USD'],
                 skiprows=1, index_col=0, parse_dates=[0])
df['CAD_USD'] = pd.to_numeric(df.CAD_USD, errors='coerce')
df.dropna(inplace=True)
df_m = df.copy()
df_m['month'] = [i.month for i in df_m.index]
df_m['year'] = [i.year for i in df_m.index]
df_m = df_m.groupby(['month', 'year']).mean()
df_m = df_m.unstack(level=0)
colors = ["#66ff66","#00ff00", "#00b300", "#008000", "#004d00", "#ff6666", "#ff0000", "#b30000" ] 
#sys.color_palette("Pastel")
fig, ax = plt.subplots(figsize=(11, 9))
sb.heatmap(df_m, cmap=colors, vmin= 0.9, vmax=1.65,
           linewidth=0.3, cbar_kws={"shrink": .8})

#cmap1 = mpl.colors.ListedColormap(['w'])
#cmap2 = mpl.colors.ListedColormap(['#0000ff'])
#cmap3 = mpl.colors.ListedColormap(["Black"])

#cbar_kws = {"ticks":df.values}
#r = sns.heatmap(df2, linewidths=.5, cmap=cmap, yticklabels=yticks, xticklabels=xticks)
#sns.heatmap(df2, mask=(df2 != 0), cbar=False, linewidths=.5, cmap=cmap1, yticklabels=yticks, xticklabels=xticks, robust=True)
#sns.heatmap(df2, mask=(df2 != -1), linewidths=.5, cbar=False, cmap=cmap2, yticklabels=yticks, xticklabels=xticks, robust=True)
#sns.heatmap(df2, mask=(df2 != -2), linewidths=.5, cbar=False, cmap=cmap3, yticklabels=yticks, xticklabels=xticks, robust=True)
#r.set_title("Heatmap")

ax.xaxis.tick_top()
xticks_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(np.arange(12) + .5, labels=xticks_labels)
plt.xlabel('')
plt.ylabel('')
title = 'monthly Average exchange rate\nValue of one USD in CAD\n'.upper()
plt.title(title, loc='left')
plt.show()
