'''
Write a python program to reverse the list :
Example:

Input: list = [4, 5, 6, 7, 8, 9]
Output : [9, 8, 7, 6, 5, 4]
'''

def reverse(lst):
    lst.reverse()
    return lst

print(reverse([4, 5, 6, 7, 8, 9]))
