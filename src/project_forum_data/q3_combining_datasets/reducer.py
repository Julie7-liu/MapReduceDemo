#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

author_id = None
reputation = None
gold = None
silver = None
bronze = None

for line in sys.stdin:
    data = line.strip().split("\t")
    source_type = data[1]

    if source_type == "A":
        author_id, source_type, reputation, gold, silver, bronze = data
    elif source_type == "B" and author_id == data[0]:
        print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(data[2], data[3], data[4], author_id, data[5], data[6], data[7], data[8], data[9], reputation, gold, silver, bronze)
