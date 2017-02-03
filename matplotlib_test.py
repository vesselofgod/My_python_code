import numpy as np
import matplotlib.pyplot as plt


N = 15
theta = np.linspace(0.0, 7 * np.pi, N, endpoint=False)
radii = 0.9 * np.random.rand(N)
width = np.pi / 3 * np.random.rand(N)

ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, width=width, bottom=0.0)

for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)

plt.show()
