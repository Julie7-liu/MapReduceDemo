#!/usr/bin/python

import sys
from datetime import datetime

#Process the purchases.txt file and outputs mean(average) of sales for each weekday

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 6:
		continue

	weekday = datetime.strptime(data[0], "%Y-%m-%d").weekday()
	sales = data[4]
	print "{0}\t{1}".format(weekday, sales)

    
