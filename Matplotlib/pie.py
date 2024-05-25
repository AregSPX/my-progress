import matplotlib.pyplot as plt
import pandas as pd

print(plt.style.available, '\n')
plt.style.use('bmh')

dict = {
    'languages': ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'],
    'popularity': [22.2, 17.6, 8.8, 8, 7.7, 6.7],
    'colors' : ['orange', 'cyan', 'grey', 'green', 'purple', 'brown']
        }
dict['languages'].reverse()
dict['popularity'].reverse()
dict['colors'].reverse()

df = pd.DataFrame(dict)

e = [0.3, 0, 0, 0, 0.1, 0]

plt.pie(df['popularity'], labels=df['languages'], shadow = True, wedgeprops={'edgecolor' : 'black'}, autopct='%1.1f%%', colors = df['colors'], explode = e)
plt.title('yoooooo, mm, yooooooooooo')
plt.show()