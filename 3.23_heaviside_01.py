##3.23
def H(x):
    if x < 0:
        H = 0
    elif x>= 0:
        H=1
        return H
def testh():
    print(H(-10), H(-1e-15), H(10))
    return
testh()