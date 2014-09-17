#!/usr/bin/env python
import sys

def main():
    if(len(sys.argv)==2):
        with open(sys.argv[1]) as f:#this should open uptimer-start.log
            for line in f:
                print line
                line = line.strip()
                print line
    else:
        print 'Usage: python uptimer.py uptimer-start.log'
        print len(sys.argv)

if __name__=="__main__":
    main()
