'''
Challenge: Reverse a String
Write a Python Program that prints the reversed version of a string.

The program must preserve uppercase and lowercase letters.

If the string is empty, print it intact
'''

def reverse_the_string(string):
    return string[::-1]

#Test case 1
sample1='Hello'
print(reverse_the_string(sample1))

#Test case 2
sample2='Wo'
print(reverse_the_string(sample2))

#Test case 3
sample3=''
print(reverse_the_string(sample3))