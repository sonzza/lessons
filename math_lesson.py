import numpy
import matplotlib.pyplot as plt

x = numpy.linspace(0, 10, 500)
k = input("введите смещение ")


y = plt.plot(x, numpy.cos(1 * x), marker='o'), plt.plot(x, numpy.cos(float(k) * x), marker='o')
plt.show(block=True)
