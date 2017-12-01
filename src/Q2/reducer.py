#!/usr/bin/python

import sys

maxVal = 0
prevKey = None

# Find the monetary value for the highest individual sale for each separate store.
for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        print "Error in mapped line, ", line
        continue

    curKey, curVal = data

    if prevKey and curKey != prevKey:
        print "{0}\t{1}".format(prevKey, maxVal)
        maxVal = 0
    
    if float(curVal) > maxVal:    
        maxVal = float(curVal)

    prevKey = curKey

if curKey:
    print "{0}\t{1}".format(curKey, maxVal)
        

