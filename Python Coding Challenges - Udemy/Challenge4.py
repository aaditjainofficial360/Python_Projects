'''
Challenge: First and Last Three Characters of a String

Write a Python program that prints the first and last three characters of the string s as a single string.

If the string has less than six characters, print an empty string (blank output).
'''

def print_one_last(string):
    if len(string)<6:
        return ''
    result=string[0:3]+string[-3:]
    return result


#Test case 1
sample1='Blue'
print(print_one_last(sample1))

#Test case 2
sample2='Wonderful'
print(print_one_last(sample2))

#Test case 3
sample3='Amazing'
print(print_one_last(sample3))