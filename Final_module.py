from matplotlib import *
from univariate_statistics import*
from two_column_text_read import*
from quadratic_fit import quadratic_fit
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from lowest_eigenvectors import*
from equations_of_state import fit_eos
from convert_units import convert_units

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


volume= convert_units(Eos_fit[0], 'cb/a')
energy= convert_units(Eos_fit[1], 'rb/a')

format_x= xlabel('X-axis')
format_y= ylabel('Y-axis')


graph = plot_data_with_fit(data, fit_curve, format_x, format_y)







#eigen_vectors= lowest_eigenvectors(square_matrix, 3)

