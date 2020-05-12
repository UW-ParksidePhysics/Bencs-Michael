from numpy import array, polyval, linspace


def fit_curve_array(eos_fit, minimum_x ,maximum_x):

        #"Make fit curve using fit polynomial coefficients, NumPy's polyval (Links to an external site.), and minimum and maximum x-values
        #        Module name:
        #                   fit_curve_array
        #       Parameters:
        #                   quadratic_coefficients: ndarray, shape (3,)
        #                   Quadratic polynomial coefficients, ordered quadratic term first, then linear term, and constant term last.
        #                   minimum_x: float
        #                   Starting value for the fit_curve array.
        #                   maximum_x: float
        #                   Ending value for the fit curve array.
        #                   number_of_points: int, optional
        #                   Number of points N to return for final fit curve. Default is 100.
        #       Returns:
        #               fit_curve: ndarray, shape (2, N)
        #               x-y data created by the coefficients of the fit function. N is the number of function evaluation points.
        #       Raises:
        #               ArithmeticError
        #               When maximum_x < minimum x.
        #               IndexError
        #               When number_of_points <= 2."

    try:
        x= linspace(minimum_x, maximum_x)


        y = eos_fit
        fit_curve= array([x, y])
        return fit_curve
    except ArithmeticError:
       print('ArithmeticError: Somethin aint addin up here')
    except IndexError:
        print('Number of points is too low')