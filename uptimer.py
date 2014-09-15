#!/usr/bin/env python
import sys

def main():
    with open(sys.argv[1]) as f:#this should open uptimer-start.log
        for line in f:
            print line

if __name__=="__main__":
    main()
