'''
Spread
Difficulty: Easy
Given a list of numbers find the spread of the list. Here, spread = Max - Min
Examples:
Test Case 1:
Input: [1,2,3,4,5]
Output: 4
Explanation: Maximum = 5, Minimum = 1. Spread = 5-1 = 4
Test Case 2:
Input: [-1,0,5]
Output: 6
Explanation: Maximum = 5, Minimum = -1. Spread = 5-(-1) = 6.
'''


def spread(lst):
    return max(lst)-min(lst)

Input1 = [1,2,3,4,5]
print(spread(Input1))

Input2 = [-1,0,5]
print(spread(Input2))