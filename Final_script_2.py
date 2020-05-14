from generate_matrix import generate_matrix
from lowest_eigenvectors import lowest_eigenvectors
from numpy import linspace
import matplotlib.pyplot as mp

potentialName = 'hamonic'
N_dim= 100
potentialParameter= 200



matrix= generate_matrix(-10, 10, N_dim, potentialName, potentialParameter)
eigenvalues, eigenvectors = lowest_eigenvectors(matrix, 1, 4)



x = linspace(-10, 10, N_dim)

def eigenvector_plot(x, eigenvectors, N_dim):
    import matplotlib.pyplot as mp

    line1, = mp.plot(x, eigenvectors[0][0:N_dim])
    line2, = mp.plot(x, eigenvectors[1][0:N_dim])
    line3, = mp.plot(x, eigenvectors[2][0:N_dim])
    display_graph= True
    mp.xlabel("x [a.u.]")
    mp.ylabel("ψ n ( x ) [a.u.]")
    mp.legend((line1, line2, line3),
              ('ψ1, Ε1 = 0.62414396 a.u.', 'ψ2, Ε2 = 0.87335307 a.u.', 'ψ3, Ε3 = 1.12229893 a.u.'))
    mp.axis([-10, 10, max(eigenvectors[0]) - 2, max(eigenvectors[0]) + 2])
    mp.axhline(color="black")  # 5
    mp.text(-9.5, -1.75, "Created by Michael 2020-05-12")  # 6
    mp.title("Select Wavefunctions for a Harmonic Potential on a Spatial Grid of 1, 2, 3 Points")  # 7
    mp.savefig("Bencs.harmonic.Eigenvector1, 2, 3.png")
    mp.show()
eigenvector_plot= eigenvector_plot(x, eigenvectors, N_dim)


print(eigenvector_plot)