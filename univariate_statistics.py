from matplotlib.pyplot import *
from numpy import *
from statistics import stdev

def univariate_statistics(data):

    if not len(data) ==2:
        print ('IndexError: data array dimensions are all wrong')
    elif (len(data[0]) or len(data[1])) <= 1:
        print('IndexError: data array dimensions are all wrong')
    else:
        min_x= min(data[0])
        max_x= max(data[0])
        min_y= min(data[1])
        max_y= max(data[1])

        # Mean
        Sum = sum(data[0]) + sum(data[1])
        Len = len(data[0]) + len(data[1])
        mean = Sum / Len

        # Standard deviation
        standard_dev= stdev(data[1])

        # Statistics
        statistics = [mean, standard_dev,
                      min_x, max_x,
                      min_y, max_y]
        return statistics




