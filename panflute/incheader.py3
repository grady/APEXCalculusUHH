#!/usr/bin/env python3

from panflute import *

def increase_header_level(elem, doc):
    if type(elem) == Header:
        if elem.level < 6:
            elem.level += 1
        else:
            return [] #  Delete headers already in level 6

def main(doc=None):
    return run_filter(increase_header_level, doc=doc)

if __name__ == "__main__":
    main()
