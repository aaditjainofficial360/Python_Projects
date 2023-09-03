'''
Challenge: Remove Spaces from a String

Write a Python program that prints a copy of the string s without any spaces.

Words should be connected in the final string.

If the string doesn't contain spaces, print it intact.
'''

def remove_spaces(string):
    if ' ' not in string:
        return string
    result = ''.join(string.split())
    return result

#Test case 1
sample1='Hello, World!'
print(remove_spaces(sample1))

#Test case 2
sample2='Have a great day'
print(remove_spaces(sample2))

#Test case 2
sample3='Python'
print(remove_spaces(sample3))