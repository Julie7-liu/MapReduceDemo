#!/usr/bin/python

import sys

#Process the purchases.txt file and outputs mean(average) of sales for each weekday

prevKey = None
salesTotal = 0
salesCnt = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    curKey, curVal = data

    if prevKey and prevKey != curKey:
        mean = salesTotal / salesCnt
        print "{0}\t{1}".format(prevKey, mean)
        salesTotal = 0
        salesCnt = 0

    prevKey = curKey
    salesTotal += float(curVal)
    salesCnt += 1

if prevKey:
    mean = salesTotal / salesCnt
    print "{0}\t{1}".format(prevKey, mean)