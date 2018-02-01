import matplotlib.pyplot as plt  
import csv
import numpy as np

#Lists
year = []
annual = []
firstQuarter = []
secondQuarter = []
thirdQuarter = []
fourthQuarter = []
# Reading data
with open('avg-temp.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if(row[0]!="YEAR"):
            year.append(int(row[0]))
            annual.append(float(row[1]))
            firstQuarter.append(float(row[2]))
            secondQuarter.append(float(row[3]))
            thirdQuarter.append(float(row[4]))
            fourthQuarter.append(float(row[5])) 
# Creating heat map
heatmap = np.empty((5, 112))
heatmap[:] = np.nan
# Updating heat map
x = 0
temp = sum(annual) / len(annual)
for T in annual:
    heatmap[0, x] = T - temp  
    x += 1

x = 0
temp = sum(firstQuarter) / len(firstQuarter)
for T in firstQuarter:
    heatmap[1, x] = T - temp 
    x += 1

x = 0
temp = sum(secondQuarter) / len(secondQuarter)
for T in secondQuarter:
    heatmap[2, x] = T - temp 
    x += 1

x = 0
temp = sum(thirdQuarter) / len(thirdQuarter)
for T in thirdQuarter:
    heatmap[3, x] = T - temp 
    x += 1

x = 0
temp = sum(fourthQuarter) / len(fourthQuarter)
for T in fourthQuarter:
    heatmap[4, x] = T - temp 
    x += 1
# Plotting
fig = plt.figure(figsize=(20,10))
ax = fig.add_subplot(111)
im = ax.imshow(heatmap, interpolation='nearest', cmap="plasma", aspect="auto")
ax.set_yticks(range(5))
ax.set_yticklabels(['ANNUAL','JAN-FEB','MAR-MAY','JUN-SEP','OCT-DEC'])
years = np.array(range(0, 112, 5))
ax.set_xticks(years)
ax.set_xticklabels(['{:d}'.format(year+1901) for year in years])
ax.set_xlabel('Years')
ax.set_title(" Average Temperature of India from 1901 to 2012")
cbar = fig.colorbar(ax=ax, mappable=im, orientation='horizontal')
cbar.set_label('Difference from Average Temperature, $^\circ\mathrm{C}$')
plt.savefig('avg-temp')
plt.show()