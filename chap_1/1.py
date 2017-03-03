# Is Unique : implement algorithm to determine if string has all unique characters.

import sys

def is_unique(s):
    d = [0 for i in range(26)]
    for c in s:
        p = ord(c.lower()) - 97
        if d[p] == 1:
            return False
        else:
            d[ord(c.lower()) - 97] += 1
    return True

print is_unique('abcd')