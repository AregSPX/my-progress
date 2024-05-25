import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

y1 = np.random.randint(1,7, size=(20,))
y2 = np.random.randint(1,7, size=(20,))
y3 = np.random.randint(1,7, size=(20,))

x = np.arange(1, 21)

plt.stackplot(x, y1 , y2, y3)

plt.show()