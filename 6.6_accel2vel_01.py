import matplotlib.pyplot as plt
import numpy as np


def velocity(a, dt):
    n = len(a)
    v = np.zeros(n)
    for k in range(1, n):
        v[k] = v[k - 1] + (a[k - 1] + a[k]) / 2
    v *= dt
    return v


acc = np.loadtxt('acc.dat')
dt = 0.1
vel = velocity(acc, dt)
time = np.array([i * dt for i in range(0, len(acc))])

plt.plot(time, acc, color='#565656', linewidth=2)
plt.plot(time, vel, color='#191919', linewidth=2)
plt.xlabel('time')
plt.legend(['Accel', 'vel'], loc=2)
plt.title('Acceleration, Time, and Velocity')
plt.show()
