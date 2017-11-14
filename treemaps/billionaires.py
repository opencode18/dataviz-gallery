# Data Manipulation
import pandas as pd
# Treemap Ploting
import squarify
# Matplotlib and Seaborn imports
import matplotlib
from matplotlib import style
import matplotlib.pyplot as plt
import seaborn as sns
# Activate Seaborn
sns.set()
# Large Plot
matplotlib.rcParams['figure.figsize'] = (16.0, 9.0)
# Use ggplot style
style.use('ggplot')

# Reading CSV file
df = pd.read_csv("rich.csv")
# Label
df["Label"] = df["Name"] + " - $" + df["Net Worth in Billion $"].astype("str") + "B"

# Change Style
style.use('fivethirtyeight')
fig, ax = plt.subplots()
# Manually Entering Colors
colors = ["#248af1", "#eb5d50", "#8bc4f6", "#8c5c94", "#a170e8", "#fba521", "#75bc3f"]
# Plot
squarify.plot(sizes=df["Net Worth in Billion $"], label=df["Label"], alpha=0.9, color=colors)
plt.axis('off')
plt.gca().invert_yaxis()
plt.title("Net Worth of World's Top 10 Billionaires", fontsize=32, color="Black")
ttl = ax.title
ttl.set_position([.5, 1.05])
fig.set_facecolor('#effeef')

plt.savefig("billionaires.png")