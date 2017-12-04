#!/usr/bin/python

import sys

#output the file's path and the number of times it appears in the log

prevKey = None
prevVal = 0
maxKey = None
maxVal = 0

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    curKey, curVal = data 

    if prevKey and prevKey != curKey:
        if prevVal > maxVal:
            maxVal = prevVal
            maxKey = prevKey

        prevVal = 0

    prevKey = curKey
    prevVal += 1

if maxKey:
   print "{0}\t{1}".format(maxKey, maxVal)
