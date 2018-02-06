import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('iitFacultyBudget.csv')
plt.style.use('ggplot')

ax = sns.barplot(x="2015-16", y="Name of Institute", data=data, label='2015-16')

plt.title("Budget Spent on Faculty Training in IITs \n for Year 2015-16")
plt.xlabel("Budget Alloted in Crores")

plt.savefig('data.png')
plt.show()
