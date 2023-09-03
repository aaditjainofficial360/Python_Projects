'''
Challenge: Check if a String Starts with a Prefix

Write a Python program that checks if the string s starts with the sequence of characters denoted by the variable prefix.

If it does, print True. Else, print False.

This test should be case sensitive. For example, "A" should not be equivalent to "a".

If the length of the prefix is greater than the length of the string, print False.
'''

def check_string_starter(string,prefix):
    if len(prefix)>len(string):
        return False
    result= string.startswith(prefix)
    return result

#Test case 1
sample1='Hello'
print(check_string_starter(sample1,prefix='He'))

#Test case 2
sample2='Coding'
print(check_string_starter(sample2,prefix='Con'))

#Test case 2
sample3='Nora'
print(check_string_starter(sample3,prefix='Circum'))
