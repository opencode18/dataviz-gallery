import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

x = []
y = []
z = []
with open("easy.txt") as f:
	while True:
		a = f.readline()
		b = f.readline()
		if not a:
			break
		p = a.split(",")
		p = [int(c) for c in p]
		p = np.array(p)
		p = p.reshape((9, 9))
		q = deepcopy(p)
		x.append(q)
		np.place(p, p>0, 1)
		y.append(p)
		r = b.split(",")
		r = [int(c) for c in r]
		r = np.array(r)
		r = r.reshape((9, 9))
		z.append(r)

x = np.array(x)
y = np.array(y)
z = np.array(z)

avg_x = np.average(x, axis=0)
avg_y = np.average(y, axis=0)
avg_z = np.average(z, axis=0)

print(avg_x)
print(avg_y)
print(avg_z)

fig = plt.figure()

ax1 = fig.add_subplot(221)

ax1.imshow(avg_x, cmap='hot', interpolation='nearest')

ax1 = fig.add_subplot(222)

ax1.imshow(avg_y, cmap='hot', interpolation='nearest')

ax2 = fig.add_subplot(223)

ax2.imshow(avg_z, cmap='hot_r', interpolation='nearest')

plt.show()