#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 6:
        print "Error in line, ", line
        continue;

    date, time, store, item, cost, payment = data
    print "{0}\t{1}".format(store, cost) 
