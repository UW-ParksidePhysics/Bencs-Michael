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
import matplotlib.pyplot as mp


#       This is the main script for part 1 in the Scientific Programming Final
#           If you are looking for part 2 look in Final_Script_2
#
#       Param: Filename: Name of File given
#              Equation of state: Birch-Murnaghan
#       Functions :  Parse_file: seperates name of file into three parts and saves as list
#                    Annotate_plot: takes Parts from name and puts them into plot as annotations
#       Returns: This script file returns the volume vs energy plot with a curve fit using the Eos_fit module
#
#       Problems: The plot will not be converted to the other unit type as I couldn't figure out what those conversions even meant
#
#       This project was one of the hardest things I have done so far in college, I would suggest that using simpler concepts \n
#               for future classes as I have not gone far enough in chemistry or math to use half these things

display_graph = True




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
min_y = statistics[4]
max_y = statistics[5]


quadratic_coefficients= quadratic_fit(data)
un_data= zip(*data)
data_list= list(un_data)


Eos_fit = fit_eos(data[0], data[1], quadratic_coefficients, eos= 'birch-murnaghan', number_of_points=50)
fit_curve= fit_curve_array(Eos_fit,min_x, max_x)
bulkmodulus= 230


volume = convert_units(data[0], 'cb/a')
energy= convert_units(data[1], 'rb/a')


def annotate_plot(chem_symb, crystal_symm, density_ex):
    import matplotlib.pyplot as mp
    annotation_chem = mp.annotate(chem_symb, xy=(200, 0.028))
    annotation_crys= mp.annotate(crystal_symm, xy=(230, -.036))
    annotation_dens= mp.annotate(density_ex, xy=(220, -.039))
    return (annotation_chem, annotation_crys, annotation_dens)


volumes = linspace(min_x, max_x, len(Eos_fit))
energy = linspace(min_y, max_y, len(Eos_fit))
volume_energy= volumes, energy


format= chem_symb, cyrstal_symm, density_ex
format_list= list(format)


curve_plot= plot_data_with_fit(data, fit_curve, volume_energy, format_list)



if display_graph == True:
    mp.savefig("Bencs.harmonic.Eigenvector1, 2, 3.png")
elif display_graph == False:
    mp.show()




