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
        

