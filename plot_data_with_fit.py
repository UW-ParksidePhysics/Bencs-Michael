def plot_data_with_fit(data, fit_curve, format_x, format_y):
    import matplotlib.pyplot as mp
    mp.title('Final Curve Plot')
    format_x
    format_y

    mp.scatter(data[0],data[1], label = 'Data', s=1)
    mp.plot(fit_curve, 'r')
    mp.show()
    return