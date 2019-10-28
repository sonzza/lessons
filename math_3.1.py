import numpy
import matplotlib.pyplot as plt
import random

# Нарисуйте график функции:
# y(x) = k∙cos(x – a) + b
x = numpy.linspace(1, 10, 100)
k = random.choice(range(10))
k1 = 4
k2 = -5
a = random.choice(range(10))
b = random.choice(range(10))


y = (k * numpy.cos(x - a) + b)
y1 = (k1 * numpy.cos(x - a) + b)
y2 = (k2 * numpy.cos(x - a) + b)
plt.plot(x, y)
plt.plot(x, y1)
plt.plot(x, y2)
plt.show(block=True)

