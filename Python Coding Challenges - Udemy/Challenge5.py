'''
Challenge: Remove Characters at Even Indices
Write a Python program that prints the string s without the characters located at even indices.

If the string is empty or only has one character, print it without any changes.
'''

def remove_even_characters(string):
    if len(string)<2:
        return string
    even_string=string[1::2]
    return even_string

#Test case 1
sample1='Coding'
print(remove_even_characters(sample1))

#Test case 2
sample2='Pizza'
print(remove_even_characters(sample2))

#Test case 3
sample3='Python'
print(remove_even_characters(sample3))

#Test case 4
sample4='A'
print(remove_even_characters(sample4))

#Test case 5
sample5=''
print(remove_even_characters(sample5))