# reads data file
from numpy import*
from os import path
def two_column_text_read(filename):

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


