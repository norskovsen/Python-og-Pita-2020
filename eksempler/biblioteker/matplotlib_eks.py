import matplotlib.pyplot as plt

xs = list(range(20))
ys = [x**2 for x in xs]
plt.plot(xs, ys)
plt.show()
