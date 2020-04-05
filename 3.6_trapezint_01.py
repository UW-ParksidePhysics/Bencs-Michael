from math import *
def trapezint1(f, a, b, actual_area):
    A = ((b - a) / 2) * (f(a) + f(b))
    print("Area beneath the curve =", A)
    error = abs(A) - abs(actual_area)
    print("Your Error =", error)
    return trapezint1

def f(x):
    f = cos(x)
    return f

a = 0; b = pi
actual_area = 0
trapezint1(f, a, b, actual_area)

def g(x):
    g = sin(x)
    return g

a = 0; b = pi
actual_area = 2
trapezint1(g, a, b, actual_area)

def h(x):
    h = sin(x)
    return h

a = 0; b = (pi / 2)
actual_area = 1
trapezint1(h, a, b, actual_area)
print()

def trapezint2(f, a, b, actual_area):
    c = b / 2
    A = ((c - a) / 2) * (f(a) + f(c)) + ((b - c) / 2) * (f(c) + f(b))
    print("Area Beneath the curve =", A)
    error = abs(A) - abs(actual_area)
    print("Error =", error)
    return trapezint2

def f(x):
    f = cos(x)
    return f

a = 0; b = pi
actual_area = 0
trapezint2(f, a, b, actual_area)

def g(x):
    g = sin(x)
    return g

a = 0; b = pi
actual_area = 2
trapezint2(g, a, b, actual_area)

def h(x):
    h = sin(x)
    return h

a = 0; b = (pi / 2)
actual_area = 1
trapezint2(h, a, b, actual_area)
print()

def trapezint(f, a, b, n, actual_area):
    x = a; A = 0; i = 0; h = (b - a) / n

    while i <= n:
        del_a = (f(a + (i * h)) + f(a + (i + 1) * h)) * (h / 2)
        A += del_a
        x += h
        i += 1
    print("Area Beneath the curve =", A)
    error = abs(A) - actual_area
    print("Error =", error)
    return trapezint

def test_trapezint():
    def f(x):
        f = cos(x)
        return f

    a = 0; b = pi
    actual_area = 0
    trapezint(f, a, b, 10, actual_area)

    def g(x):
        g = sin(x)
        return g

    a = 0; b = pi
    actual_area = 2
    trapezint(g, a, b, 10, actual_area)

    def h(x):
        h = sin(x)
        return h

    a = 0; b = (pi / 2)
    actual_area = 1
    trapezint(h, a, b, 10, actual_area)
    return test_trapezint

test_trapezint()