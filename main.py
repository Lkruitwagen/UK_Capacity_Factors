import sys
import re
import os
import commands
import urllib2
import csv


def main(argv):

    print 'hellloooo'
    print sys.argv
    key=argv[0]
    url = 'https://api.bmreports.com/BMRS/B1610/v1?APIKey='+key+'&SettlementDate=2016-08-08&Period=4&ServiceType=csv'
    response = urllib2.urlopen(url)
    cr = csv.reader(response)

    print 'hellloooo'

    for row in cr:
        print row



if __name__=='__main__':

  main(sys.argv[1:])
