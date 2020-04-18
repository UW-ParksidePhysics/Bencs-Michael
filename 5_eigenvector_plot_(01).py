from math import sqrt, exp, pi
from numpy import linspace, linalg, sqrt, sin, pi, sum, zeros, diag
import matplotlib.pyplot as mp



#problem 2
x = linspace(0, 10, 200)


def y1(x):
    y1 = (1 / (0.5 * sqrt(2 * pi))) * 2.71828 ** ((-1 / 2) * ((x - 5) / 0.5) ** 2)
    return y1


def y2(x):
    y2 = (1 / (1.0 * sqrt(2 * pi))) * 2.71828 ** ((-1 / 2) * ((x - 5) / 1.0) ** 2)
    return y2


def y3(x):
    y3 = (1 / (1.5 * sqrt(2 * pi))) * 2.71828 ** ((-1 / 2) * ((x - 5) / 1.5) ** 2)
    return y3


mp.plot(x, y1(x), label='σ = 0.5')
mp.plot(x, y2(x), label='σ = 1.0')
mp.plot(x, y3(x), label='σ = 1.5')

mp.xlabel('0 <= x <= 10')
mp.ylabel('Φ(x-5,σ)')
mp.legend()
mp.title('Problem 2')
mp.axis([0, 10, 0, 1])
mp.show()

##Problem 3
from numpy import zeros, linalg, linspace, sqrt, sin, pi
import matplotlib.pyplot as mp
A = zeros([5, 5])

n = 0
while n <= 5 - 1:
    A[n, n] = 2
    n = n + 1

n = 0
while n <= 3:
    A[n, n + 1] = 1
    A[n + 1, n] = 1
    n = n + 1

H = (1 / (2 * (1 / (5 - 1)) ** 2)) * A
dx = 5/(5+1)

(V, D) = linalg.eig(H)
B = D[:, [4]]
C = sqrt(sum(B**2)*dx)
E = B/C
x = linspace(1/(5+1), 5/(5+1), 5)


def y(x):
    y = sqrt(2) * sin(pi * x)
    return y


mp.plot(x, E)  # Blue Graph
mp.plot(x, y(x))  # Orange Graph
mp.show()

#Problem 4

npoints = int(input('What npoints? '))
var = max(10, npoints)
A = zeros([var, var])

n = 0
while n <= var-1:
    A[n, n] = 2
    n = n + 1

n = 0
while n <= var-2:
    A[n, n + 1] = 1
    A[n + 1, n] = 1
    n = n + 1


H = (1 / (2 * (1 / (var - 1)) ** 2)) * A
dx = var/(var+1)

(V, D) = linalg.eig(H)
B = D[:, [-1]]
C = sqrt(sum(B**2)*dx) # Normalization constant
E = B/C
x = linspace(1/(var+1), var/(var+1), var)


def y(x):
    y = sqrt(2) * sin(pi * x)
    return y


mp.plot(x, E)  # Blue Graph
mp.plot(x, y(x))  # Orange Graph
mp.show()


