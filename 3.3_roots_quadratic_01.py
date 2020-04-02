from numpy.lib.scimath import sqrt
from numpy import roots
a = eval(input("What is your a value? "))
b = eval(input("What is your b value? "))
c = eval(input("What is your c value? "))

List = [a, b, c]
R = roots(List)

print (R)
print ()
print ()


D2 = (b**2) - (4*a*c)
if a == 0:
    print('a cannot be equal to zero')

if D2 >= 0:
    D = sqrt(D2)
    x1 = (-b - D) / (2 * a)
    x2 = (2 * c) / (-b - D)
    R = [x1, x2]
    print("float")
    print(R)

elif D2 < 0:
    D2 = -D2
    D = (sqrt(D2) / (2 * a))
    b2 = -b / (2 * a)
    print("complex")
    print(b2, "+", D, "j", b2, "-", D, "j")