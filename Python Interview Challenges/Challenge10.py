'''
Given a list of numbers, the task is to write a Python program to find the second largest number in the given list.

Examples:

Input: list1 = [10, 20, 4]
Output: 10

Input: list2 = [70, 11, 20, 4, 100]
Output: 70
'''

def second_largest(lst):
    second_large=max([x for x in lst if x!=max(lst)])
    return second_large

print(second_largest([10, 20, 4]))

print(second_largest([70, 11, 20, 4, 100]))