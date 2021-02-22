#!/usr/bin/env python3

from panflute import *
import re

pattern = re.compile(r'^(ex|thm|def|fig)[:_](.+)')

envs = {'exm': 'example', 'thm': 'theorem', 'def': 'definition', 'fig': 'geogebra'}

def deemph(e, doc):
    if isinstance(e, Emph):
        return list(e.content)

def theorems(e, doc):
    if type(e) == Div:
        cls = envs.get(e.classes[0])
        if cls is None:
            return
        if doc.format == 'markdown':
            ident = pattern.search(e.identifier)
            ii = label = echo = ''
            if ident:
                ii = re.sub('_','-', ident.group(2)) 
                label = ', label="' + ii + '"'
            if cls != 'geogebra':
                echo = ', echo=TRUE'
            left = RawBlock('```{'+ cls + label + echo + '}', format='markdown')
            right = RawBlock('```', format='markdown')
            #e = e.walk(deemph)
        else:
            return
        
        e.content[0].content.pop(0)
        e.content[0].content.pop(0)
        # e.content = [left] + list(e.content) + [right]
        return list([left] + list(e.content) + [right])

    

if __name__ == "__main__":
    toJSONFilter(theorems)
