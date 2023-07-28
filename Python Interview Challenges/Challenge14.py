'''
Given the start and end of a range, write a Python program to print all negative numbers in a given range.

 Examples:

Input: a = -4, b = 5
Output: -4, -3, -2, -1

Input: a = -3, b= 4
Output: -3, -2, -1
'''

def print_negative_nos(start,end):
    if end<0:
        for i in range(start,end+1):
            if i!=end:
                print(i,end=', ')
            else:
                print(i,end='')
    else:
        for i in range(start,0):
            if i!=-1:
                print(i,end=', ')
            else:
                print(i,end='')
    return ''

# Input: a = -4, b = 5
print(print_negative_nos(-4,5))

# Input: a = -3, b= 4
print(print_negative_nos(-3,4))