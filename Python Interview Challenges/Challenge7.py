'''
Given start and end of a range, write a Python program to print all positive numbers in given range.

Example:

Input: start = -4, end = 5
Output: 0, 1, 2, 3, 4, 5

Input: start = -3, end = 4
Output: 0, 1, 2, 3, 4
'''

def print_positive_no(start,end):
    if start>=0:
        for i in range(start,end+1):
            if i!=end:
                print(i,end=', ')
            else:
                print(i,end='')
    else:
        for i in range(0,end+1):
            if i!=end:
                print(i,end=', ')
            else:
                print(i,end='')
    return ''

print(print_positive_no(start=-4,end=5))

print(print_positive_no(start=-3,end=4))