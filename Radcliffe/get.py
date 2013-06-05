# Module: get.py
#
# Called from: process_alias.py, process_supervision.py,
#              process_conviction.py, process_criminal_record.py
#
# This module contains helper functions that extend the find and
# findall methods in xml.etree.cElementTree.
#
# Examples:
#     node(elt, 'a/b/c') is equivalent to elt.find('a').find('b').find('c')
#     text(elt, 'a/b/c') is equivslent to elt.find('a').find('b').find('c').text
#     All(elt,  'a/b/c') is equivalent to elt.find('a').find('b').findall('c')
#
# Pretty cool, ain't it?


def node(elt, path = None):
    if path:
        for tag in path.replace(' ','').split('/'):
            child = elt.find(tag)
            if child != None:
                elt = child
            else:
                return None
    return elt

def text(elt, path = None):
    x = node(elt, path)
    if x != None:
        return x.text

def All(elt, path):
    l = path.rsplit('/',1)
    if len(l) == 1:
        return elt.findall(l[0])
    else:
        return node(elt, l[0]).findall(l[1])

def Alltext(elt, path):
    return [x.text for x in All(elt, path) if x.text != None]
        

