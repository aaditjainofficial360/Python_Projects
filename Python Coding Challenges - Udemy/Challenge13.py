'''
Challenge: Check if a String Ends with a Suffix

Write a Python program that checks if the string s ends with a specific sequence of characters denoted by the variable suffix.

If it does, print True. Else, print False.

This test should be case sensitive. Therefore, "A" should not be equivalent to "a".

If the length of the suffix is greater than the length of the string, print False.
'''

def check_string_terminator(string,suffix):
    if len(suffix)>len(string):
        return False
    result=string.endswith(suffix)
    return result

#Test case 1
sample1='Hello'
print(check_string_terminator(sample1,suffix='ello'))

#Test case 2
sample2='Coding'
print(check_string_terminator(sample2,suffix='eng'))

#Test case 2
sample3='Nora'
print(check_string_terminator(sample3,suffix='rowing'))