def lowest_eigenvectors(square_matrix, number_of_eigenvectors):
    from numpy import linalg, argsort
    #Identify eigenvectors with smallest K eigenvalues given input matrix using NumPy's eig  (Links to an external site.)function
    #       Module name:
    #                    lowest_eigenvectors
    #       Parameters:
    #                   square_matrix: ndarray, shape(M, M)
    #                   Matrix to be characterized. Must be a square matrix of M rows and M columns where M is >=1.
    #                   number_of_eigenvectors: int, optional
    #                   Number of eigenvectors K with eigenvalues to return.  Default is 3.
    #       Returns:
    #               eigenvalues: ndarray, shape(K,)
    #               Array of the K lowest-value eigenvalues ordered from lowest to highest.
    #                eigenvectors: ndarray, shape(K, M)
    #               Array of K eigenvectors with M components arranged in order corresponding to their eigenvalues. The first index should correspond to the eigenvalue index in the eigenvalues array. The order of the components in the eigenvector remains the same as output by NumPy's eig.

    def lowest_eigenvectors(square_matrix, starting_index, ending_index):
        from numpy import linalg, linspace, sqrt, sin, pi, sum, sort, argsort






        M_rows = len(square_matrix)
        count = 0
        while count < M_rows:
            M_columns = len(square_matrix[count])
            if not M_rows == M_columns:
                return print("Must be a square matrix of M rows and M columns where M is >= 1.")
            count += 1

        (V, D) = linalg.eig(square_matrix)
        ordered_indices = argsort(V)
        eigenvalues = (V[ordered_indices[starting_index:ending_index]])  # [0:number_of_eigenvectors]
        eigenvectors = (D[ordered_indices[starting_index:ending_index]])  # ^^^
        return eigenvectors