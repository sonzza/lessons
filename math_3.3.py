import numpy
import matplotlib.pyplot as plt
import math

R = int(input("Введите радиус "))
a = int(input("Введите угол "))
x = R * numpy.cos(a)
y = R * numpy.sin(a)

print("x равен ", x, " y равен ", y)

# окружность в полярных координатах
x1 = []
x2 = []
y1 = []
y2 = []
dots = 360
for i in range(dots):
    y_ = i * (R / dots)
    x_ = math.sqrt(math.fabs(math.pow(R, 2) - math.pow(y_, 2)))
    x1.append(x_)
    y1.append(y_)
    x2.append(-x_)
    y2.append(-y_)

plt.polar(x1, y1)
plt.polar(x1, y2)
plt.polar(x2, y1)
plt.polar(x2, y2)
plt.show(block=True)

# прямая в полярных координатах раскоментить при закоменчивании окружности
# c = numpy.linspace(0, 10, 500)
# b = c**2
# plt.polar(c, b)
# plt.show(block=True)
