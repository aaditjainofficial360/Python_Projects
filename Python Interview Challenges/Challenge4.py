'''
Given a list of numbers, write a Python program to print all positive numbers in given list.

Example:

Input: list1 = [12, -7, 5, 64, -14]
Output: [12, 5, 64]

Input: list2 = [12, 14, -95, 3]
Output: [12, 14, 3]
'''

def positive_nos(lst):
    positive_nos=[x for x in lst if x>=0]
    return positive_nos

print(positive_nos([12, -7, 5, 64, -14]))

print(positive_nos([12, 14, -95, 3]))