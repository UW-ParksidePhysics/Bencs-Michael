from matplotlib import *
from univariate_statistics import*
from two_column_text_read import*
from quadratic_fit import quadratic_fit
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from lowest_eigenvectors import*
data = two_column_text_read('volumes_energies.dat')

statistics= univariate_statistics(data)

mean = (statistics[0])
standard_deviation= statistics[1]
min_x = statistics[2]
max_x = statistics[3]
min_y = statistics[4]
max_y = statistics[5]

quadratic_coefficients= quadratic_fit(data)

fit_curve = fit_curve_array(quadratic_coefficients ,min_x ,max_x)

format_x= xlabel('X-axis')
format_y= ylabel('Y-axis')
graph = plot_data_with_fit(data,fit_curve, format_x,format_y)

square_matrix= ([1,2],[3,4])
eigen_vectors= lowest_eigenvectors(square_matrix, 3)

print(eigen_vectors)