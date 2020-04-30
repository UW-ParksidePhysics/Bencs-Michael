##4.2
##f2c_cml.py
## author is Michael Bencs

import sys

try:
    F=float(sys.argv[1])
    C=(5.0/9)*(F-32)
    print (C)
except IndexError:
    raise IndexError('I think you are forgetting something')

