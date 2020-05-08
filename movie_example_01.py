import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from numpy import exp, pi, sqrt, linspace

fig = plt.figure

#use example 5.3.4 for hint
def f(x, m, s):
    return (1.0 / (sqrt(2*pi)*s))*exp(-0.5*((x-m)/s)**2)

m = 0
s_min = 1
s_max = -1
x = linspace(m -6*s_max, m + 6*s_max, 1000)
s_values = linspace(s_max, s_min, 30)
max_f = f(m, m, s_min)

#make plot, then animation
plt.ion()
y = f(x, m, s_max)
lines = plt.plot(x,y)
plt.axis([x[0], x[-1], -0.1,max_f])
plt.xlabel('x')
plt.ylabel('f')

counter = 0
for s in s_values:
    y = f(x, m, s)
    lines[0].set_ydata(y)
    plt.legend(["s={:1f}".format(s)])
    plt.draw()
    plt.savefig('tmp_{:0>4}.png'.format(counter))
    counter += 1
