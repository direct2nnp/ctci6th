'''
Palindrome Permutation -> Given a string, write a function to check if it is a permutation
of a palindrome. 
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
'''

def Palindrome_permutation(s):
    d = [0 for i in range(26)]
    for c in s:
        if c != ' ':
            d[ord(c.lower()) - 97] += 1

    print d
    flag = False
    for e in d:
        if e % 2 != 0:
            if flag == False:
                flag = True
            else:
                return False

    return True


print Palindrome_permutation('Tact Coa')
print Palindrome_permutation('Hello World')