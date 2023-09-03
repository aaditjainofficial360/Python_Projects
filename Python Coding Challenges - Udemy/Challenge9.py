'''
Challenge: Change Commas by Dots

Write a Python program that prints a version of the string s with all commas replaced by dots.
'''

def replace_commas(string):
    string=string.replace(',','.')
    return string

#Test case 1
sample1='Hello, World!'
print(replace_commas(sample1))

#Test case 2
sample2='3,456,344'
print(replace_commas(sample2))