'''
Given a list, write a Python program to swap first and last element of the list.

Examples:

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
'''

def swapelement(lst):
    lst[0],lst[-1]=lst[-1],lst[0]
    return lst

print(swapelement([12, 35, 9, 56, 24]))

print(swapelement([1, 2, 3]))