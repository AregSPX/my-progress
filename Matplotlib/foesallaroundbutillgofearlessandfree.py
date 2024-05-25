import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('puk.csv', parse_dates=True)

plt.style.use('fivethirtyeight')

print(df)

print(df.dtypes)

plt.plot(df['Date'], df['Close'], linewidth = 0.8)
plt.gcf().autofmt_xdate()

plt.xlabel('Date')
plt.ylabel('Closing Value')
plt.title('Closing stock value, Alphabet Inc.')


plt.grid(True)
plt.tight_layout()

plt.show()