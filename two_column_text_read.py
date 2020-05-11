# reads data file
def two_column_text_read(str):
    infile = open(str, 'r').readlines()


def x_column(infile):
    two_column_text_read(str)
    xlines = infile.readlines()
    result = []
    for x in xlines:
        result.append(x.split('  ')[1])
        print(x)


def y_column(y):
    lines = infile.readlines()
    result = []
    for y in lines:
        result.append(y.split('  ')[2])
        print(y)

#    print(infile)


#       column1 = float(lines.split()[2]).append(column1)
#       column2 = float(lines.split()[2]).append(column2)
#       print( '% % ' %(column1, column2))
