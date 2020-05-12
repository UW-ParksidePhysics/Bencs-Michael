def quadratic_fit(data):
    from numpy import polyfit
    x= data[0]
    y= data[1]
    for i in range(len(data)):
        quadratic_coefficients = polyfit(x, y, 2)
    return quadratic_coefficients
