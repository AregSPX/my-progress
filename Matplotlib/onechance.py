import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('puk.csv', parse_dates=True, index_col='Date')

df.plot()

plt.title('Sample Graph!')
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.legend()

plt.tight_layout()

plt.show()