import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')

dict = {
    'languages': ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'],
    'popularity': [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        }
dict['languages'].reverse()
dict['popularity'].reverse()

df = pd.DataFrame(dict)

print(df)

plt.barh(df['languages'], df['popularity'])


plt.title('Lang-Pop')
plt.ylabel('Popularity in %')
plt.grid(True)

plt.tight_layout()

plt.show()



