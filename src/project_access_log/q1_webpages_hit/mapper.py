#!/usr/bin/python

import sys

# To display the number of hits for each different file on the web site, this mapper extracts the website filename

for line in sys.stdin:
    data = line.strip().split(" ")

    if len(data) != 10:
        continue

    ip, id, username, date, zone, method, url, protocol, status, size = data
    print "{0}\t{1}".format(url,1)


