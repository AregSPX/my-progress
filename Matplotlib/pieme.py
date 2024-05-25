import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('bmh')

df = pd.read_csv('medal.csv')
print(df)

e = [0.2, 0, 0, 0, 0]


plt.pie(df['gold_medal'], labels = df['country'], wedgeprops = {'edgecolor': 'black'}, shadow = True, autopct='%1.1f%%', explode = e, startangle = 328)

plt.show()