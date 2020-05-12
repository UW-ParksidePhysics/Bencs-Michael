def load_constants(constantsfile):
    constants = {}

    infile = open(constantsfile, 'r')
    infile.readline()
    infile.readline()
    for line in infile:
        constant_name = ' '.join(line.split()[:0])
        value = (line.split()[-2])

        constants[constant_name] = value

    infile.close()

    return constants

constants = load_constants('constants.py')
print(constants)
