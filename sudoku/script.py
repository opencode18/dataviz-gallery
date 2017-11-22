import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy


def empty_spaces(fl):
	x = []
	y = []
	z = []
	with open(fl) as f:
		while True:
			a = f.readline()
			b = f.readline()
			if not a:
				break
			p = a.split(",")
			p = [int(c) for c in p]
			p = np.array(p)
			p = p.reshape((9, 9)).T
			q = deepcopy(p)
			x.append(q)
			np.place(p, p>0, 1)
			y.append(p)
			r = b.split(",")
			r = [int(c) for c in r]
			r = np.array(r)
			r = r.reshape((9, 9)).T
			z.append(r)

	x = np.array(x)
	y = np.array(y)
	z = np.array(z)

	avg_x = np.average(x, axis=0)
	avg_y = np.average(y, axis=0)
	avg_z = np.average(z, axis=0)

	return avg_y


easy = empty_spaces("easy.txt")
medium = empty_spaces("medium.txt")
hard = empty_spaces("hard.txt")
evil = empty_spaces("evil.txt")

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.imshow(easy, cmap="hot", interpolation="nearest")
ax1.title.set_text("Easy")
ax1.axis("off")

ax2 = fig.add_subplot(222)
ax2.imshow(medium, cmap="hot", interpolation="nearest")
ax2.title.set_text("Medium")
ax2.axis("off")

ax3 = fig.add_subplot(223)
ax3.imshow(hard, cmap="hot", interpolation="nearest")
ax3.title.set_text("Hard")
ax3.axis("off")

ax4 = fig.add_subplot(224)
ax4.imshow(evil, cmap="hot", interpolation="nearest")
ax4.title.set_text("Evil")
ax4.axis("off")

ttl = "Heatmap of 250 Sudoku Puzzles by Difficulty"

plt.suptitle(ttl, fontsize=16)

cap = "Darker = More likely to be empty"

fig.text(.5, .05, cap, ha="center", fontsize=14)

plt.savefig("final_lot.png", dpi=300)

plt.show()