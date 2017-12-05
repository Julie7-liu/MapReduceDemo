#!/usr/bin/python

import sys
import csv
import re

#Creates an index of all words that can be found in the body of a forum post and node id they can be found in

reader = csv.reader(sys.stdin, delimiter='\t')
#writer = csv.writer(sys.stdout, delimiter='\t', quotechar='""', quoting=csv.QUOTE_ALL)

for line in reader:
    nodeId = line[0]
    body = line[4]
    words = re.split('[^a-zA-Z0-9\']+', body)

    for word in words:
        word = word.strip().lower()

        if len(word) > 0:
            print "{0}\t{1}".format(word, nodeId)

    
