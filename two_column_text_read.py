# reads data file
from numpy import*
from os import path
def two_column_text_read(filename):
    #"Read in two columns of data from a text file of arbitrary length
    #   Module name:
    #       two_column_text_read
    #   Parameters:
    #       filename: str
    #       Name of file to be read in.
    #   Returns:
    #           data: ndarray, shape (2, M)
    #           x-y data read in from file. M is the number of data points.
    #   Raises:
    #           OSError
    #           When filename cannot be found for reading.
    #



    if path.exists(filename):
        infile = open(filename, 'r')
        x= []
        for line in infile:
            str= line.split()
            x1 = [float(x) for x in str]
            x.append(x1)
        infile.close()
        unzip_x = zip(*x)
        x= list(unzip_x)

        data = array(x)
        return data
    else:
        return print('OSError: the filename entered was not found')


