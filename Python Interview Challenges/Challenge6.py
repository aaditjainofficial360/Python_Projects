'''
Given a list of numbers, write a Python program to print all negative numbers in the given list.

Example:

Input: list1 = [12, -7, 5, 64, -14]
Output: [-7, -14]

Input: list2 = [12, 14, -95, 3]
Output: [-95]
'''

def negativenos(lst):
    negativenos=[x for x in lst if x<0]
    return negativenos

print(negativenos([12, -7, 5, 64, -14]))

print(negativenos([12, 14, -95, 3]))