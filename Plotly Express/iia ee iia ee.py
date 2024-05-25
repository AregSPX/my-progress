import plotly.express as px
import pandas as pd 
import numpy as np 
from plotly.subplots import make_subplots as subplots

df = pd.read_csv('C:/Users/User/OneDrive/Рабочий стол/processing/Matplotlib/puk.csv')
print(df)

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%y')
print(df.dtypes)

L = [df['Open'], df['High'], df['Low'], df['Close']]
PL = []


titles = ['Open', 'High', 'Low', 'Close']
labels = [{'x' : 'Date', 'y' : 'Opening Price'}, {'x' : 'Date', 'y': 'High Price'},
           {'x' : 'Date', 'y' : 'Low Price'}, {'x' : 'Date', 'y' : 'Closing Price'}]
          
#Problem: how to make this work if i have to write i + 1 and i at the same time, in result of which the last graph gets thrown out.
for i in range(3):
    PL.append(px.line(x = df['Date'], y = df.iloc[:, i + 1], title = titles[i], labels = labels[i]))


#Problem: how to make this work (i want a sublot out of those graphs)
fig = subplots(rows = 1, cols= 3)

for i in range(3):
    fig.add_trace(PL[i], row = 1, col= i+1)

fig.show()

#for i in range(4):
    #PL[i].show()

