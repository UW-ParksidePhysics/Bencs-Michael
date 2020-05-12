from numpy import array, polyval
def fit_curve_array(quadratic_coefficients,minimum_x ,maximum_x):


   try:
        x= list(range(minimum_x, maximum_x))
        x_array= array(x)

        fit_curve = polyval(quadratic_coefficients, x_array)
        return fit_curve
   except ArithmeticError:
       print('ArithmeticError: Somethin aint addin up here')