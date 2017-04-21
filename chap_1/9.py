'''
String Rotation:Assume you have a method isSubstring which checks if one word is a substring of another. 
Given two strings, sl and s2, write code to check if s2 is a rotation of sl 
using only one call to isSubstring

Example : "waterbottle" is a rotation of"erbottlewat"
'''
def isSubstring(s1, s2):
    if s2 in s1:
        return True
    else:
        return False

def isRotation(s1, s2):
    if len(s2) == len(s1) and len(s2) > 0:
        return isSubstring(s1+s1, s2)
    else:
        return False

print isRotation('waterbottle', 'erbottlewat')
print isRotation('abcdef', 'asdasas')