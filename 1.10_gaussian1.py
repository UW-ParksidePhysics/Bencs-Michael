from math import exp, sqrt, pi

m = 0
s = 2
x = 1

prefactor = 1/(sqrt(2*pi) *s)
exponential_argument = -(1/2)*((x-m)/s)**2

f = prefactor * exp(exponential_argument)
print(f)
