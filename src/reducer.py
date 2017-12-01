#!/usr/bin/python

import sys

valTotal = 0
prevKey = None

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        print "Error in mapped line, ", line
        continue

    curKey, curVal = data

    if prevKey and curKey != prevKey:
        print "{0}\t{1}".format(prevKey, valTotal)
        valTotal = 0
    
    valTotal += float(curVal)
    prevKey = curKey

if curKey:
    print "{0}\t{1}".format(curKey, valTotal)
        

