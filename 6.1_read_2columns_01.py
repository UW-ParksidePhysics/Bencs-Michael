import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

infile = open('xy.dat', 'r')
for line in infile:
    coords = line.split()
    x.append(float(coords[0]))
    y.append(float(coords[1]))
infile.close()

x, y = np.array(x), np.array(y)

print('Minimum x value = {:.4f}'.format(x.min()))
print('Maximum x value = {:.4f}'.format(x.max()))
print('Minimum y value = {:.4f}'.format(y.min()))
print('Maximum y value = {:.4f]'.format(y.max()))

plt.plot(x, y, color='#19999', linewidth=2.0)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
