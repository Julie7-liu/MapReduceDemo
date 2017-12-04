#!/usr/bin/python

import sys

#Find the most popular file on the website
path_strip = "http://www.the-associates.co.uk"

for line in sys.stdin:
    data = line.strip().split(" ")

    if len(data) != 10:
        continue

    ip, id, username, date, zone, method, path, protocol, status, size = data
    if path_strip in path:
        path = path.replace(path_strip, "")
    print "{0}\t{1}".format(path, 1)


