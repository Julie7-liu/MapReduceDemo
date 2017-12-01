#!/usr/bin/python

import sys

#Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 6:
        print "Error in line, ", line
        continue;

    date, time, store, item, cost, payment = data
    print cost 
