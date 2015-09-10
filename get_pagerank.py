#!/usr/bin/env python
# Author: Muneeb Ali | http://muneeb.org
# WARNING: Mining PageRank is against Google's Terms of Service
# DISCLAIMER: This wrapper/script was written for teaching students about PageRank and is not meant for commercial use

import sys
from pagerank import GetPageRank


def my_func(input):

    pagerank = GetPageRank(input)
    pagerank = pagerank.split(':')

    site_pagerank = 0

    try:
        site_pagerank = pagerank[2].rstrip('\n')
    except:
        site_pagerank = 0

    print "PageRank of " + input + " is: " + str(site_pagerank)


def usage():
    print 'Usage: {prog} <url>'.format(prog=sys.argv[0])
    return -1

if __name__ == "__main__":

    if len(sys.argv) != 2:
        usage()
    else:
        my_func(sys.argv[1])
