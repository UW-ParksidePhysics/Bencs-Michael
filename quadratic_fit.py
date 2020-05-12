def quadratic_fit(data):
    #"Fit a quadratic polynomial to a two row Numpy array of x-y data using Numpy's polyfit (Links to an external site.) function
    #    Module name:
    #               quadratic_fit
    #   Parameters:
    #                data: ndarray, shape (2, M)
    #               x-y data to be fit. M is the number of data points.
    #    Returns:
    #          quadratic_coefficients: ndarray, shape (3,)
    #           Quadratic polynomial coefficients, ordered quadratic term first, then linear term, and constant term last."



    from numpy import polyfit
    x= data[0]
    y= data[1]
    quadratic_coefficients = polyfit(x, y, 2)
    return quadratic_coefficients
