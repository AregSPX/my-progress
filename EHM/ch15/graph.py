import matplotlib.pyplot as plt

x = range(1,5001)
y = [x**3 for x in x]


fig, ax = plt.subplots()
ax.scatter(x, y, c = y, cmap = plt.cm.Blues, s = 10)

ax.set_title('AregSPX', fontsize = 20)
ax.set_xlabel('x', fontsize = 15)
ax.set_ylabel('y', fontsize = 15)

ax.ticklabel_format(style = 'plain')

plt.show()

