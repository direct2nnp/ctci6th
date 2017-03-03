# Check Permutations : Given two strings, write a method to decide if one is a permutations of other

import sys

def check_permutation(a,b):
    if len(a) != len(b):
        return False

    d = [0 for i in range(26)]

    for c in a:
        d[ord(c) - 97] += 1

    for c in b:
        if d[ord(c) - 97] <= 0:
            return False
        else:
            d[ord(c) - 97] -= 1

    return True


print check_permutation('aaa', 'aaa')