import matplotlib.pyplot as plt
import numpy
import math


# 1.2 задание длина вектора
# A = int(input("Введите начальную координату: "))
# B = int(input("Введите конечную координату: "))
#
# print("Длина вектора равна: {}".format(B - A))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# 3 задание окружность
x = numpy.linspace(0, 10, 360)
x1 = []
y1 = []
points = []
round_center = input("Введите центр окружности (через пробел): ")
R = input("Введите радиус: ")
a = float(round_center.split()[0])
b = float(round_center.split()[1])
for i in range(360):
    tmp_x = 0
    tmp_y = 0
    plt.plot(tmp_x, tmp_y)
    x1.append(tmp_x)
    y1.append(tmp_y)
    points.append(Point(tmp_x, tmp_y))
#     x_ = i / 360
#     x1.append(x_)
#     y_ = i / 360
#     y1.append(math.sqrt(math.pow((x_ - a), 2) + math.pow((y_ - b), 2)))
#     y2.append(-math.sqrt(math.pow((x_ - a), 2) + math.pow((y_ - b), 2)))
# print(x1)
# print(y1)
# print(y2)

# circle = plt.Circle((a, b), 0.2, linewidth=1, fill=False)
# fig, ax = plt.subplots()
# ax.add_artist(circle)
plt.plot(x1, y1)
for point in points:
    plt.plot(point.x, point.y)
# plt.plot(x1, y2)
#
# plt.xlabel("x")
# plt.ylabel("y")
plt.show(block=True)
