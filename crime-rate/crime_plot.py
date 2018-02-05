
import matplotlib.pyplot as plt  
import csv
import numpy as np

plt.style.use('ggplot')
states = []
crime_2016 = []


x = 0
with open('crime.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if row[0] != "S. No. (Col.1)":
            states.append(row[2])
            crime_2016.append(float(row[6]))
            
                    

fig = plt.figure()
plt.bar(states, crime_2016, color='#004177')
plt.setp(plt.gca().get_xticklabels(), rotation = 30, horizontalalignment='right')
plt.tight_layout()
plt.xlabel('States')
plt.ylabel('Crime Rate(%)')
plt.title("Crime Rates in Different States (2016)")
fig = plt.gcf()
fig.set_size_inches(16, 8)
plt.savefig('crime-rate')
plt.show()

