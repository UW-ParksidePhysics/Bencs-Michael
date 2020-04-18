import numpy as np
import matplotlib.pyplot as plt
plt.plot(t, y)
plt.legend(['t^2exp(-t^2)'])
plt.xlabel('t')
plt.ylabel('y')
plt.axis([0, 3, -0.5, 0.6])   #[tmin, tmax, ymin, ymax]
plt.title('My First Matplotlib Demo')
plt.show()
plt.savefig('tmp2.pdf')  #produces pdf
plt.plot(t, y, label= 't^2*exp(-t^2)')

def f1(t):
    return t**2*np.exp(-t**2)
def f2(t):
    return t**2*f1(t)

t = np.linespace(0, 3, 51)
y1 = f1(t)
y2 = f2(t)

plt.plot(t, y1, 'r-')
plt.plot(t, y2, 'bo')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['t^2*exp(-t^2)', 't^4*exp(-t^2)'])
plt.title('Plotting tow curves in the same plot')
plt.savefig('tmp3.pdf')
plt.show()