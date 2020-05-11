def quadratic_fit(data):
    from numpy import polyfit

    quadratic_coefficients = polyfit(data[0], data[1], 2)
    return quadratic_coefficients