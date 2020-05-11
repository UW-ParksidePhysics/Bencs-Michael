from numpy import array, polyval
def fit_curve_array(quadratic_coefficients,minimum_x ,maximum_x):


   try:
        x = [minimum_x, maximum_x]
        fit_curve = polyval(quadratic_coefficients, x)
        return fit_curve
   except ArithmeticError:
       print('ArithmeticError: Somethin aint addin up here')