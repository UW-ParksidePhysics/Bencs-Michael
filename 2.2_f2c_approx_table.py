print('------------------')
F = 0
dF = 10
while F <= 100:
    C = (5 / 9) * (F - 32)
    C_hat = (F-30)/2
    print('{}\t{:.2f}\t{:.2f}'.format(F, C, C_hat))
    F = F + dF
print('------------------')
