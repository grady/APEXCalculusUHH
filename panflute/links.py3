#!/usr/bin/env python3

from panflute import *
import re

def links(e, doc):
    if type(e) == Link:
        if doc.format == 'markdown':
            url = e.url.strip('#')
            url = re.sub('_', '-', url)
            url = re.sub('ex[:-]', 'exm:', url)
            return RawInline('\@ref(' + url + ')', format='markdown')

if __name__ == "__main__":
    toJSONFilter(links)
