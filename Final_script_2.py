from generate_matrix import generate_matrix
from lowest_eigenvectors import lowest_eigenvectors
from numpy import linspace
import matplotlib.pyplot as mp

#       This is the main script for part 2 in the Scientific Programming Final
#           If you are looking for part 1 look in Final_Script_1
#
#       Param: Potential Name: Name of  given
#              Numbers of dimensions: Number of dimensions given by Final data
#              Potential Parameter: 200
#
#       Functions :  eigenvector_plot: plots the lowest eigen vectors for as many dimensions given
#       Returns: This script file returns a graph of a harmonic functions lowest eigen vectors from 1 to 3
#
#       Problems: little to no annotations so I apologize if its confusing
#
#       This project was one of the hardest things I have done so far in college, I would suggest that using simpler concepts \n
#               for future classes as I have not gone far enough in chemistry or math to use half these things





display_graph= True


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

eigenvector_plot= eigenvector_plot(x, eigenvectors, N_dim)


if display_graph == True:
    mp.savefig("Bencs.harmonic.Eigenvector1, 2, 3.png")
elif display_graph == False:
    mp.show()