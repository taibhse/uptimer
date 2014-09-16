#!/usr/bin/env python
import sys

def main():
    print len(sys.argv)
    with open(sys.argv[1]) as f:#this should open uptimer-start.log
        for line in f:
            print line
            line = line.strip()
            print line

if __name__=="__main__":
    main()
