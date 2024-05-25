import matplotlib.pyplot as plt
import pandas as pd
import datetime
from matplotlib import dates as mpl_dates

plt.xkcd()

df = pd.read_csv('puk.csv')
df['Date'] = pd.to_datetime(df['Date'])
print(df.dtypes)
print(df)

fig1, (ax1, ax2) = plt.subplots(2,1, sharex = True)
fig2, (ax3, ax4) = plt.subplots(2,1, sharex = True)
ax1.plot(df['Date'], df['Open'], label = 'Open')

ax2.plot(df['Date'], df['High'], label = 'High', color = 'red')

ax3.plot(df['Date'], df['Low'], label = 'Low', color = 'gold')

ax4.plot(df['Date'], df['Close'], label = 'Close', color = 'green')

ax1.set_title('some shit')
fig1.autofmt_xdate()
fig2.autofmt_xdate()

dafor = mpl_dates.DateFormatter('%d-%b-%Y')
ax1.xaxis.set_major_formatter(dafor)
ax2.xaxis.set_major_formatter(dafor)
ax3.xaxis.set_major_formatter(dafor)
ax4.xaxis.set_major_formatter(dafor)

ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()

plt.tight_layout()

plt.show()



