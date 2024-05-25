import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
ages = {
    'Men' : [22, 30, 35, 35, 26],
    'Women' : [25, 32, 30, 35, 29],
    'Groups' : range(1,6)
        }
df = pd.DataFrame(ages, index=range(1,6))

plt.barh(df['Groups'], df['Men'], color = 'blue')
plt.barh(df['Groups'],  df['Women'], left = df['Men'], color = 'pink')

#df.plot(kind='bar')

plt.show()
