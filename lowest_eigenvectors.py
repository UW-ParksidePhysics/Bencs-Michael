from numpy import *
def lowest_eigenvectors(square_matrix, number_of_eigenvectors):
    from numpy import zeros, linalg, linspace, sqrt, sin, pi, sum, sort
    import numpy as np

    M_rows = len(square_matrix)  # Function statement, only works in a function
    count = 0
    while count < M_rows:
        M_columns = len(square_matrix[count])
        if not M_rows == M_columns:
            return print("Must be a square matrix of M rows and M columns where M is >=1.")
        count += 1

    number_of_eigenvectors=3
    A = zeros([10,10])

    n = 0
    while n <= 9:
        A[n, n] = 2
        n = n + 1

    n = 0
    while n <= 8:
        A[n, n + 1] = 1
        A[n + 1, n] = 1
        n = n + 1


    H = (1 / (2  (1 / 9 * 2))) * A
#print (H)


    (V, D) = linalg.eig(H)
    ordered_indices= argsort(V)
#print(ordered_indices)

#print(V[ordered_indices[0:3]])
#print(D[ordered_indices[0:3]])

    return ordered_indices