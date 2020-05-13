from matplotlib import *
from univariate_statistics import*
from two_column_text_read import*
from quadratic_fit import quadratic_fit
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from lowest_eigenvectors import*
from equations_of_state import fit_eos
from convert_units import convert_units
from generate_matrix import generate_matrix


def parse_file(filename):
    axis_names= filename.split('.')
    chem_symb = axis_names[0]
    crystal_symm = axis_names[1]
    density_ex = axis_names[2]
    return chem_symb, crystal_symm, density_ex

filename= 'Sn.Fd-3m.GGA-PBE.volumes_energies.dat'
data = two_column_text_read(filename)
data= data/ 2

chem_symb, cyrstal_symm, density_ex = parse_file(filename)





statistics= univariate_statistics(data)

mean = (statistics[0])
standard_deviation= statistics[1]
min_x = statistics[2]
max_x = statistics[3]


quadratic_coefficients= quadratic_fit(data)

Eos_fit = fit_eos(data[0], data[1], quadratic_coefficients, eos= 'birch-murnaghan')

fit_curve = fit_curve_array(Eos_fit, min_x, max_x)


#volume = convert_units(Eos_fit[0], 'cb/a')
#energy= convert_units(Eos_fit[1], 'rb/a')

format_x= xlabel('E  eV/atom')
format_y= ylabel('V  A^3/atom')

#energy_volume= plot_data_with_fit(volume, energy, format_x, format_y)
data_curve = plot_data_with_fit(data, fit_curve, format_x, format_y)


start, end, N_dim, potential_name, potential_parameter= (-10,10, 90, 'harmonic', 100)
matrix= generate_matrix(start, end, N_dim, potential_name, potential_parameter)


eigenvectors= lowest_eigenvectors(matrix, 1)


x = linspace(-10, 10, len(eigenvectors[0][0:N_dim]))

def eigenvector_plot(x, eigenvectors, N_dim):
    import matplotlib as mp

    line1, = mp.plot(x, eigenvectors[0][0:N_dim])  # 4
    line2, = mp.plot(x, eigenvectors[1][0:N_dim])  # 4
    line3, = mp.plot(x, eigenvectors[2][0:N_dim])  # 4
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
eigenvector_plot= eigenvector_plot(x, eigenvectors, N_dim )




