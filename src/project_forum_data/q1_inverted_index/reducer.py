#!/usr/bin/python

import sys

#Creates an index of all words that can be found in the body of a forum post and node id they can be found in

prevWord = None
nodeSet = set()

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    word, nodeId = data
    if prevWord and word != prevWord:
        nodeList = list(nodeSet)
        nodeList.sort()
        print "{0}\t{1}".format(prevWord, ",".join(str(node) for node in nodeList))
        nodeSet = set()
        
    nodeSet.add(nodeId)
    prevWord = word

if prevWord:
	nodeList = list(nodeSet)
	nodeList.sort()
	print "{0}\t{1}".format(prevWord, ",".join(str(node) for node in nodeList))

