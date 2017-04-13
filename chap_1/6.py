'''
String Compression - Implement a method which perform basic string compression using the 
count of repeated character

Example:
aabcccccaaa -> a2b1c5a3
return smaller length string between original and compressed
'''

def is_compressed(a):
    len_a = len(a)
    new_s = ''
    counter = 0
    for i in range(len_a-1):
        if a[i] == a[i+1]:
            counter += 1
        else:
            new_s += a[i] + str(counter+1)
            counter = 0
    
    # handling last character match 
    if a[-1] == a[-2]:
        new_s += a[i] + str(counter+1)
    else:
        new_s += a[-1] + str(1)

    return True if len(a) >= len(new_s) else False 


print is_compressed('aabcccccaaa')
print is_compressed('abcdef')