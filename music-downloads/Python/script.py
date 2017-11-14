
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np

data = pd.read_csv('digital-sells.csv')

data["Total Digital Downloads"] = data["Total Digital Downloads"] / 1000000

mpl.rcParams['figure.figsize'] = (9, 40)
mpl.style.use('fivethirtyeight')

ax = sns.barplot(x="Total Digital Downloads", y="Music Artist", data=data)
for index, row in data.iterrows():
    ax.text(row["Total Digital Downloads"], index, int(1000000*row["Total Digital Downloads"]), va="center")
plt.title("Digital Music Downloads of Various Music Artists", fontsize=32)
plt.xlabel("Total Downloads in Million")
ttl = ax.title
ttl.set_position([.5, 1.02])
plt.tight_layout(pad=1.5, h_pad=1.2, w_pad=1.2)
plt.savefig("final_plot.png", dpi=300)
