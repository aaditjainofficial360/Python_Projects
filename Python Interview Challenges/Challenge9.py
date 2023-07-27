'''
Given a list, print the value obtained after multiplying all numbers in a list.

Examples:

Input :  list1 = [1, 2, 3]
Output : 6
Explanation: 1*2*3=6

Input : list1 = [3, 2, 4]
Output : 24
'''

from functools import reduce
def multiply_product(lst):
    product=reduce(lambda x,y:x*y,lst)
    return product

print(multiply_product([1, 2, 3]))

print(multiply_product([3, 2, 4]))

