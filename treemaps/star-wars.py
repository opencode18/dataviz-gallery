import pandas as pd
import squarify
import matplotlib
from matplotlib import style
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

matplotlib.rcParams['figure.figsize'] = (16.0, 9.0)

df = pd.read_csv("starwars-revenue.csv")
df = df.sort_values(by="Revenue", ascending=False)
df["Percentage"] = round(100 * df["Revenue"] / sum(df["Revenue"]), 2)
df["Label"] = df["Label"] + " (" + df["Percentage"].astype("str") + "%)"

fig, ax = plt.subplots()
cmap = matplotlib.cm.coolwarm
mini = min(df["Revenue"])
maxi = max(df["Revenue"])
norm = matplotlib.colors.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in df["Revenue"]]
squarify.plot(sizes=df["Revenue"], label=df["Label"], alpha=0.8, color=colors)
plt.axis('off')
plt.gca().invert_yaxis()
plt.title("Revenue from Star Wars Franchise Movies", fontsize=32)
ttl = ax.title
ttl.set_position([.5, 1.05])
fig.set_facecolor('#eeffee')

plt.savefig("star-wars.png")