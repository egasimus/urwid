# this is part of the subproc.py example

import sys
if sys.version > '3':
    xrange = range

num = int(sys.argv[1])
for c in xrange(1,10000000):
    if num % c == 0:
        print("factor:", c)
