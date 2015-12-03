# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): [ dct[x] for x in keylist ]

def list2dict(L, keylist): { x:y for x,y in zip(keylist,L) }
