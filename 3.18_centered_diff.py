from math import *
##A##
def diff(f,x,h):
    d= ((f(x+h) - f(x-h)) / (2*h))
    return d


##C##
def application(f , x, h, exactDerivative):
    derivative = diff(f, x, h)
    error = exactDerivative - derivative
    print("___________")
    print("Approximate Derivative =", derivative)
    print("Exact Derivative =", exactDerivative)
    print(derivative, "-", exactDerivative, "=", error)
    return
def f(x):
    f = exp(x)
    return f
def g(x):
    g = exp(-2 * (x**2))
    return g
def h(x):
    h = cos(x)
    return h
def i(x):
    i = log(x)
    return i
application(f, 0, .01, 1)
application(g, 0, .01, 0)
application(h, (2*pi), .01, 0)
application(i, 1, .01, 1)
##B##
def a(x):
    a= 4*x**4
    return a
application(a, 0, .01, 0)


