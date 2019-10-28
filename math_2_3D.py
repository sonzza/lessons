import numpy
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
ax1 = Axes3D(fig)
X = numpy.arange(-15, 15, 0.1)
Y = numpy.arange(-15, 15, 0.1)
X, Y = numpy.meshgrid(X, Y)
Z = X + Y
# ax.plot_wireframe(X, Y, Z)            # Раскоментить после закоменчивания от Z1 до ax1 в 20 строчке
# ax.plot_wireframe(10 + X, 10 + Y,  Z)
# plt.show(block=True)

Z1 = 6*X**2+2*Y**2
Z2 = numpy.sqrt(X**2+Y**2)

ax1.plot_surface(X, Y, Z1)
ax1.plot_surface(X, Y, Z2)

plt.show(block=True)