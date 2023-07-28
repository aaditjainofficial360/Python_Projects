'''
Given a list of numbers of list, write a Python program to create a list of tuples having first element as the number and second element as the cube of the number.

Example:

Input: list = [1, 2, 3]
Output: [(1, 1), (2, 8), (3, 27)]

Input: list = [9, 5, 6]
Output: [(9, 729), (5, 125), (6, 216)]
'''

def create_cube_tuple(lst):
    out_lst=[(x,x**3) for x in lst]
    return out_lst

print(create_cube_tuple([1, 2, 3]))

print(create_cube_tuple([9, 5, 6]))