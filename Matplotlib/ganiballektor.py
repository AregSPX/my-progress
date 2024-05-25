import matplotlib.pyplot as plt
import pandas as pd

print(plt.style.available)
plt.style.use('bmh')

x1 = [10, 20, 30, 40, 50, 60]
y1 = [20, 5, 10, 25, 40, 55]
y2 = [40, 10, 30, 45, 60, 75]


plt.plot(x1, y1, label = 'line 1')
plt.plot(x1, y2, label = 'line 2')

plt.title('with suitable legends')
plt.xlabel('x - axis')
plt.ylabel('y - axis')


plt.legend()

plt.tight_layout()

plt.show()

