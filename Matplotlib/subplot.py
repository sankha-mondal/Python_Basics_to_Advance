#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(nrows=1, ncols=2)

## plot-1
xpoints1 = np.array([2020, 2021, 2022, 2023, 2024])
ypoints1 = np.array([6.6, 7.7, 8.5, 7.0, 6.8])
ax[0].plot(xpoints1,ypoints1,color='green')


## Plot-2
xpoints2 = np.array([2020, 2021, 2022, 2023, 2024])
ypoints2 = np.array([-4.5, 3.7, 4.0, 7.0, 9.8])
ax[1].plot(xpoints2,ypoints2,color='red')

plt.show()  # To show the graph

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
