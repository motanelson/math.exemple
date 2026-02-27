import matplotlib.pyplot as plt

plt.style.use('dark_background')

n = list(range(10))
m = [x * 2 for x in n]

plt.scatter(n, m)
plt.show()