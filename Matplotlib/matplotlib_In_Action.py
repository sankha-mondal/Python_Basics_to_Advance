#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([2020, 2021, 2022, 2023])
ypoints = np.array([6.6, 8.7, 7.0, 6.8])

plt.title('Indias GDP by Year')
plt.xlabel('Year')
plt.ylabel('GDP')
plt.grid(color='green',linestyle='--',linewidth=1,axis='y')
plt.plot(xpoints, ypoints,color='red')
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
