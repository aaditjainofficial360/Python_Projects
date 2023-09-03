'''
Challenge: Replace a Character in a String

Write a Python program that prints the string s with the character curr_char replaced by the character new_char.

curr_char and new_char are variables that contain strings with a single character.

You may assume that new_char will not be an empty string.

The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).

If no match is found, print the initial string.
'''

def replace_character(string,curr_char,new_char):
    string=string.replace(curr_char,new_char)
    return string

#Test case 1
sample1='Hello'
print(replace_character(sample1,curr_char='I',new_char='s'))

#Test case 2
sample2='World'
print(replace_character(sample2,curr_char='W',new_char='A'))

#Test case 3
sample3='Python'
print(replace_character(sample3,curr_char='P',new_char='x'))

#Test case 4
sample4='Python'
print(replace_character(sample4,curr_char='p',new_char='a'))