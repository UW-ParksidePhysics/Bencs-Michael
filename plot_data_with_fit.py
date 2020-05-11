def plot_data_with_fit(data, fit_curve, format_x, format_y):
    import matplotlib.pyplot as mp
    mp.title('Final Curve Plot')
    format_x
    format_y

    mp.plot(data[0],data[1], 'b')
    mp.plot(fit_curve[0], fit_curve[1], 'r+')
    mp.show()
    return