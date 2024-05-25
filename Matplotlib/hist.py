import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.arange(11)
y = np.random.randint(0, 10, size = (10000,))

plt.hist(y, bins = x, edgecolor = 'black')
plt.xticks(ticks = x)

plt.show()