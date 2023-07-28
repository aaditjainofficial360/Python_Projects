'''
Given a list of numbers, write a Python program to count positive and negative numbers in a List.

Example:

Input: list1 = [2, -7, 5, -64, -14]
Output: pos = 2, neg = 3

Input: list2 = [-12, 14, 95, 3]
Output: pos = 3, neg = 1
'''

def counting_numbers(lst):
    positive_count=0
    negative_count=0
    for i in lst:
        if i!=0:
            if i>0:
                positive_count+=1
            else:
                negative_count+=1
    result='pos = '+str(positive_count)+', neg = '+str(negative_count)
    return result

list1 = [2, -7, 5, -64, -14]
print(counting_numbers(list1))

list2 = [-12, 14, 95, 3]
print(counting_numbers(list2))