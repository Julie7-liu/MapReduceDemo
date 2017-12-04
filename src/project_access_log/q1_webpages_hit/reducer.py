#!/usr/bin/python

import sys

# To display the number of hits for each different file on the web site

prevUrl = None
prevCnt = 0

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    curUrl, cnt = data 

    if prevUrl and prevUrl != curUrl:
        print "{0} {1}".format(prevUrl, prevCnt)
        prevCnt = 0

    prevUrl = curUrl
    prevCnt += 1

if prevUrl:
   print "{0}\t{1}".format(prevUrl, prevCnt)
