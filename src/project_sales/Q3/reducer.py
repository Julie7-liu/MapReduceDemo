#!/usr/bin/python

import sys

#Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.

sumVal = 0
sumCnt = 0

for line in sys.stdin:
    curVal = float(line)

    sumVal += curVal
    sumCnt += 1

print "{0}\t{1}".format(sumVal,sumCnt)

