'''
URLify - write a method to replace all spaces in string with '%20'
Input = 'Mr John Smith ', 13
output = "Mr%20John%20Smith"
'''

def URLify(old, l):
    end = False
    new = ['' for i in range(l)]
    for i in reversed(old):
        if i != ' ' and end == False:
            end = True

        if end == True:
            if i != ' ':
                new[l-1] = i
                l -= 1
            elif i == ' ':
                new[l-1] = '0'
                new[l-2] = '2'
                new[l-3] = '%'
                l = l - 3

    return ''.join(new)


print URLify('Mr John Smith    ', 17)