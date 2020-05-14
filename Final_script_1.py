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
un_data= zip(*data)
data_list= list(un_data)

Eos_fit = fit_eos(data_list[0], data_list[1], quadratic_coefficients, eos= 'birch-murnaghan', number_of_points=50)


fit_curve = fit_curve_array(Eos_fit, min_x, max_x)

un_data= zip(*data)
data_list= list(un_data)

bulkmodulus= 230

volume = convert_units(Eos_fit[0], 'cb/a')
energy= convert_units(Eos_fit[1], 'rb/a')

def annotate_plot(chem_symb):
    import matplotlib.pyplot as mp
    annotation = mp.annotate('hello', xy=(-0.46, 100))
    return annotation

#energy_volume= plot_data_with_fit(volume, energy, format_x, format_y)
data_curve = plot_data_with_fit(data, fit_curve)


start, end, N_dim, potential_name, potential_parameter= (-10,10, 90, 'harmonic', 100)



eigenvectors= lowest_eigenvectors(matrix, 1)


volumes = linspace(min(data_list[0]), max(data_list[0]), len(Eos_fit))





