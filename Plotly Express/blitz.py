import plotly.express as px
from plotly.subplots import make_subplots as subplots
import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/User/OneDrive/Рабочий стол/processing/Matplotlib/puk.csv', index_col='Date')

fig = px.line(df, labels = {'y': 'Price'})

ar = px.scatter_3d(x = np.arange(0,11), y = np.arange(0,11), z = np.arange(0,11))
print(df)
fig.show()

ar.show()







#Some day.
#fig = subplots(rows = 1, cols = 2)
#fig.append_trace(line1, row = 1, col=1)
#fig.show()
