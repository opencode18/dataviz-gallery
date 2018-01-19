import numpy as np
import  csv

import matplotlib.pyplot as plt
from matplotlib import dates, ticker
import matplotlib as mpl
from matplotlib.finance import candlestick_ohlc

mpl.style.use('default')

fname = 'maruti.csv'

date_data = []
open_data = []
high_data = []
low_data = []
close_data = []

with open(fname, 'r') as csvfile:
	data = csv.reader(csvfile, delimiter=',')
	for line in data:
		date_data.append(line[0])
		open_data.append(line[1])
		high_data.append(line[2])
		low_data.append(line[3])
		close_data.append(line[4])

open_val = np.array(open_data[1:], dtype=np.float64)
high_val = np.array(high_data[1:], dtype=np.float64)
low_val = np.array(low_data[1:], dtype=np.float64)
close_val = np.array(close_data[1:], dtype=np.float64)

data_dates = []

for date in date_data[1:]:
	new_Date = dates.datestr2num(date)
	data_dates.append(new_Date)

i=0
ohlc_data = []

while i<len(data_dates):
	stats_1_day = data_dates[i], open_val[i], high_val[i], low_val[i], close_val[i]
	ohlc_data.append(stats_1_day)
	i +=1

dayFormatter = dates.DateFormatter('%d-%b-%Y')

fig, axl = plt.subplots()

candlestick_ohlc(axl, ohlc_data, width=0.5, colorup='g', colordown='r', alpha=0.75)

axl.xaxis.set_major_formatter(dayFormatter)
axl.xaxis.set_major_locator(ticker.MaxNLocator(10))
plt.xticks(rotation=30)
plt.xlabel('DATE')
plt.ylabel('Price in Rupees')
plt.title('Historical Data for MARUTI SUZUKI EQUITY \n in BSE from period 01-10-2017 to 18-01-2018')
plt.tight_layout()

plt.grid()
plt.savefig('graph.jpg')
