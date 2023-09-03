'''
Challenge: Print the Character at a Specific Index

Write a Python program that prints the character at index i in the string s.

If the index is out of range, the program should print "i is out of range"

If the string is empty, the program should print "Empty String"
'''

def print_character(string,index):
    if string=='':
        return 'Empty String'
    elif index>=len(string):
        return 'index is out of range'
    return string[index]

#Test case 1
sample1='Hello'
print(print_character(sample1,2))

#Test case 2
sample2='Pizza'
print(print_character(sample2,4))

#Test case 3
sample3=''
print(print_character(sample3,3))

#Test case 4
sample4='World'
print(print_character(sample4,15))


