#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

# Histogram - It is a frequency distribution graph, the y-axis represent the count.

student_scores = np.array([80,90,88,22,34,90,80,70,60,80,77,66,90])
plt.hist(student_scores, rwidth=0.5)
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
