# A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter
# in the alphabet within the string; ie: b occurs no more times than a; c occurs no more times than b; etc.
# Note that letter a has no previous letter.
#
# Given a string, check whether it is beautiful.

def isBeautifulString(inputString):
    index = 0
    counter = 0
    while index < len(inputString):
        if inputString[index] == 'a':
            index += 1
        else:
            c = inputString.count(chr(ord(inputString[index])-1))
            if c >= inputString.count(inputString[index]):
                counter += 1
                index += 1
            else:
                return False
    g = inputString.count('a')
    if counter == (len(inputString) - g):
        return True