import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#x = np.random.randint(1, 501, size = (500,))
#y = np.random.randint(1, 501, size = (500,))
#sa = np.random.randint(1, 1501, size = (500,))


#plt.scatter(x, y, s = sa, c = sa, cmap = 'Greens', edgecolors='black', alpha=0.4)


D = {
    'math_marks' : [88, 92, 80, 89, 100, 80, 60, 100, 80, 34],
    'science_marks' : [35, 79, 79, 48, 100, 88, 32, 45, 20, 30],
    'marks_range' : [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}



df = pd.DataFrame(D)

LD = [D['math_marks'], D['science_marks']]
LTest = ['green', 'blue'] 
Labels = ['Math', 'Science']
for i in range(0, 2):
    plt.scatter(df['marks_range'], LD[i], color = LTest[i], s = 45, label = Labels[i])

plt.title('Marks') 
plt.xlabel('Marks Range')
plt.ylabel('Marks Scored')
plt.legend()




plt.show()

