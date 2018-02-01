# Visualisation for number of 3, 4 and 5 star hotels in different states in the year 2013, 2014 and 2015
import matplotlib.pyplot as plt  
import csv
import numpy as np

plt.style.use('ggplot')
#Lists
states = []
star1 = []
star2 = []
star3 = []
star4 = []
star5 = []
# Reading data
x = 0
with open('hotel.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if(row[0] != "Category"):
            states.append(row[1])
            star1.append(int(row[10]))
            star2.append(int(row[20]))
            star3.append(int(row[30]))
            star4.append(int(row[40]))
            star5.append(int(row[50]))            
X = range(29)
star10 = np.array(star1)
star20 = np.array(star2)
star30 = np.array(star3)
star40 = np.array(star4)
star50 = np.array(star5)
# Plotting
fig = plt.figure()
plt.bar(states, star5, label="3 stars", color='#000B14', bottom=star10+star20+star30+star40)
plt.bar(states, star4, label="4 stars", color='#002A4C', bottom=star10+star20+star30)
plt.bar(states, star3, label="3 stars", color='#004177', bottom=star10+star20)
plt.bar(states, star2, label="2 stars", color='#ED6200', bottom=star10)
plt.bar(states, star1, label="1 star", color='#FF8800')
plt.legend(loc ="upper right")
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
plt.yticks([i for i in range(0, 400, 20)])
plt.tight_layout()
plt.xlabel('States')
plt.ylabel('Number of Hotels')
plt.title("Number hotels in different states in the year 2015")
plt.show()
