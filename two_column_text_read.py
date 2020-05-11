# reads data file
def two_column_text_read(file, column):
    infile= open('file', 'r')
    lines= infile.readlines()
    result= []
    for number in lines:
        result.append(number.split(' ')[1])
    infile.close()


