#!/usr/bin/python3
def islower(c):
    c = ord(c)
    if (ord('a') <= c and c <= ord('z')):
        return True
    else:
        return False
