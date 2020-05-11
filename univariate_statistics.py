from matplotlib.pyplot import *
from numpy import *

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
        data_stan = data
        count = 0
        count2 = 0
        count3 = 0
        while count < Len:  # IDK if standard deviation accounts for both x and y, but I did that here.
            data_stan[count2][count3] = (data_stan[count2][count3] - mean) ** 2
            count += 1
            count3 += 1
            if count == Len / 2:
                count3 = 0
                count2 += 1
        Sum_stan = sqrt(sum(data_stan[0]) ** 2 + sum(data_stan[1]) ** 2)
        Len_stan = sqrt(len(data_stan[0]) ** 2 + len(data_stan[1]) ** 2)
        standard_deviation = sqrt(Sum_stan / Len_stan)

        # Statistics
        statistics = [mean, standard_deviation,
                      min_x, max_x,
                      min_y, max_y]
        return statistics




