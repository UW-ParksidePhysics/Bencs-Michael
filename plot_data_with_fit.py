def plot_data_with_fit(data, fit_curve, volume_energy, annotations):
    #Create a combined scatter and curve plot for the data and the fit polynomial, respectively, using Pyplot's plot (Links to an external site.) function
    #    module name:
    #               plot_data_with_fit
    #    Parameters:
    #               data: ndarray, shape(2, M)
    #               x-y data that was fit. M is the number of data points.
    #               fit_curve: ndarray, shape(2, N)
    #               x-y data created by the coeffecients of the fit function. N is the number of function evaluation points (usually much greater than M).
    #               data_format: str, optional
    #               Optional formatting specification for the style of the scatter plot data points.  Default is ''.  See Pyplot's plot (Links to an external site.) for specifications.
    #               fit_format: str, optional
    #               Optional formatting specification for the curve of the fit function. Default is ''.  See Pyplot's plot (Links to an external site.) for specifications.
    #       Returns:
    #               combined_plot
    #               A list of Line2D (Links to an external site.) objects representing the plotted data. This is the default return type from Pyplot's plot.
    #



    import matplotlib.pyplot as mp

    title=('Birch-murnaghan Equation of State for ', annotations[0], 'in DFT ', annotations[2])
    mp.title(title)





    line1 = mp.plot(data[0], data[1], 'o')
    line2= mp.plot(volume_energy[0], volume_energy[1],'r+')
    line3= mp.plot(fit_curve[0],fit_curve[1], 'black')


    s1= annotations[0]
    s2= annotations[1]
    s3= annotations[2]
    mp.text(205, -163.228, s1)
    mp.text(230, -163.236, s2)
    mp.text(220, -163.239, s3)


    mp.xlabel(r'$ \mathcal{eV/atom}\ $')
    mp.ylabel(r'$ \mathit{Å^3/atom}\ $')
    #mp.legend((line1, line2, line3), ('Data= o', 'Volume vs Energy= Red +', 'Eos Fit= Black') )
    mp.text(-9.5, -1.75, "Created by Michael 2020-05-14")






    return