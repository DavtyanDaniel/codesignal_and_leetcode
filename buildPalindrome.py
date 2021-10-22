# Given a string, find the shortest possible string which can be
# achieved by adding characters to the end of initial string to make it a palindrome.


def buildPalindrome(st):
    l = list(st)
    removeelements = []
    if l == l[::-1]:
        return ''.join(l)
    removeelements.insert(0,l[0])
    print (removeelements)
    l = l[1::]
    print(l)
    print (''.join(l) + ''.join(removeelements))
    return ''.join(removeelements) + buildPalindrome(''.join(l)) + ''.join(removeelements)