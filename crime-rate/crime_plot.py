import matplotlib.pyplot as plt  
import pandas as pd
from pandas import DataFrame
import numpy as np


plt.style.use('ggplot')

df = pd.read_csv('crime.csv')  

fig = plt.figure()


plt.bar(df['State/UT (Col.3)'], df['Percentage Share of State/UT (2016) (Col.7)'], color='#004177')
plt.setp(plt.gca().get_xticklabels(), rotation = 30, horizontalalignment='right')
plt.tight_layout()
plt.xlabel('States')
plt.ylabel('Crime Rate(%)')
plt.title("Crime Rates in Different States (2016)")
fig = plt.gcf()
fig.set_size_inches(16, 8)
plt.savefig('crime-rate')
plt.show()

