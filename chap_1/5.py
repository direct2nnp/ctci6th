'''
One Away - There are three types of edit can be performed on string.
    insert a char
    remove a char
    replace a char

Given two string, Write a function to check if they are one edit or zero edit away

EXAMPLE
pale, ple -> true 
pales, pale -> true 
pale, bale -> true 
pale, bake -> false
'''

def OneAway(a, b):
    if abs(len(a) - len(b)) > 1:
        return False

    edit = 0
    done = True
    x = 0
    y = 0

    while(done):
        if a[x] == b[y]:
            x += 1
            y += 1
        else:
            if edit == 1:
                return False
            else:
                if a[x+1] == b[y]:
                    edit += 1
                    x += 1
                elif a[x] == b[y+1]:
                    edit += 1
                    y += 1
                elif a[x+1] == b[y+1]:
                    edit += 1
                    x += 1
                    y += 1
                else:
                    return False

    return True

print OneAway('pale', 'ple')

