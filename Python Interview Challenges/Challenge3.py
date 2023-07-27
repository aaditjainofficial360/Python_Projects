'''
Given a list of numbers, write a Python program to count Even and Odd numbers in a List.

Example:

Input: list1 = [2, 7, 5, 64, 14]
Output: Even = 3, odd = 2

Input: list2 = [12, 14, 95, 3]
Output: Even = 2, odd = 2
'''

def count_odd_even(lst):
    even_lst=[x for x in lst if x%2==0]
    odd_lst=[y for y in lst if y%2!=0]
    even_count,odd_count=len(even_lst),len(odd_lst)
    result="Even = "+str(even_count)+", odd = "+str(odd_count)
    return result

print(count_odd_even([2, 7, 5, 64, 14]))

print(count_odd_even([12, 14, 95, 3]))