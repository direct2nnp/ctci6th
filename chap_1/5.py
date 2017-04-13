'''
One Awapos_b - There are three tpos_bpes of edit can be performed on string.
    insert a char
    remove a char
    replace a char

Given two string, Write a function to check if thepos_b are one edit or zero edit awapos_b

EXAMPLE
pale, ple -> true 
pales, pale -> true 
pale, bale -> true 
pale, bake -> false
'''

def OneAway(a, b):
    if abs(len(a) - len(b)) > 1:
        return False

    loop_counter = min(len(a), len(b))

    edit = False
    done = True
    pos_a = 0
    pos_b = 0

    for i in range(loop_counter):
        if a[pos_a] == b[pos_b]:
            pos_a += 1
            pos_b += 1
        else:
            if edit == True:
                return False
            else:
                edit = True
                if len(a) > len(b):
                    pos_a += 1
                elif len(a) < len(b):
                    pos_b += 1
                else:
                    pos_a += 1
                    pos_b += 1

    return True 

print OneAway('pale', 'ple')
print OneAway('pale', 'pale')
print OneAway('pale', 'bale')
print OneAway('pale', 'bake')

