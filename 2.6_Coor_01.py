l = []
n = eval(input("What does n equal :"))
x1 = eval(input("what is the 1st coordinate :"))
x2 = eval(input("What is the 2nd coordinate :"))
i = 0
for i in range(n):
    h = (x2 - x1) / n
    x = (x1) + i * h
    l.append(x)
    i += 1
print(l)
