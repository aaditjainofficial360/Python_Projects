'''
Challenge: Check if a String Only Contains Numbers

Write a Python program that check if a string only contains numbers.

If it does, print True. Else, print False.
'''

def check_nos_instring(string):
    return string.isdigit()

#Test case 1
sample1='Hello'
print(check_nos_instring(sample1))

#Test case 2
sample2='4567'
print(check_nos_instring(sample2))

#Test case 3
sample3='Hello59'
print(check_nos_instring(sample3))

#Test case 4
sample4=''
print(check_nos_instring(sample4))