#!/usr/bin/python

import sys

# Display the number of hits to the site made by each different IP address

prevKey = None
prevVal = 0

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    curKey, curVal = data 

    if prevKey and prevKey != curKey:
        print "{0} {1}".format(prevKey, prevVal)
        prevVal = 0

    prevKey = curKey
    prevVal += 1

if prevKey:
   print "{0}\t{1}".format(prevKey, prevVal)
