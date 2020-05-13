def plot_data_with_fit(data, fit_curve, format_x, format_y):
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
    mp.title('Final Curve Plot')
    format_x
    format_y

    mp.scatter(data[0],data[1],  label = 'Data', s=1,)
    mp.plot(fit_curve[0],fit_curve[1], 'black')
    mp.show()
    return