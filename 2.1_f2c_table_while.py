print('------------------')
F = 0
dF = 10
while F <= 100:
    C = (5 / 9) * (F - 32)
    print('{}\t{:.2f}'.format(F, C))
    F = F + dF
print('------------------')
