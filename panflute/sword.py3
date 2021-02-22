#!/usr/bin/env python3

from panflute import toJSONFilter, Str, RawInline, Strong
from pylatexenc.latexwalker import LatexWalker
import re

pattern = re.compile(r'\\ref{(.+)}')

def sword(elem, doc):
    if type(elem) == RawInline and elem.format == 'latex':
        pass
        w,_,_ = LatexWalker(elem.text[1:]).get_latex_nodes()
        try:
            if w[0].macroname == 'sword':
                return Str(r'\@ref('+w[1].latex_verbatim()+r')')
        except AttributeError:
            pass
        # result = pattern.search(elem.text)
        # if result:
        #     return Str(r'\@ref('+result.group(1)+r')')
        

    
if __name__ == "__main__":
    toJSONFilter(sword)
