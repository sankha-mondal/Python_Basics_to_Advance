#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([2020, 2021, 2022, 2023, 2024])
ypoints = np.array([6.6, 7.7, 8.5, 7.0, 6.8])

plt.title('Indias GDP by Year')
plt.xlabel('Year')
plt.ylabel('GDP')
plt.grid(color='green',linestyle='--',linewidth=1,axis='y',alpha=0.5)

## Generate Line Plot:
plt.plot(xpoints, ypoints,color='red',alpha=0.8,linestyle='--',linewidth=5)

## Generate Scatter Graph:
plt.scatter(xpoints,ypoints,color='blue')

## Generate Bar Graph:
plt.bar(xpoints,ypoints,color='orange')

plt.show()  # To show the graph

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
