'''
Locate Peak
Difficulty: Medium
Question: Given a list of integers, find the index of the maximum value. If there are two maximums, return index of the first one. If given list is empty return -1. Do not use the index() method.
Examples:
Test Case 1:
Input - [5, 10, 15, 4, 6]
Output - 2
Explanation - The maximum number is 15. It’s index is 2.
Test Case 2:
Input - [22,3,22,2,7,11]
Output - 0
Explanation - There are two maximums with value 22. The first one has index 0.
'''

def locate_peak(lst):
    if lst!=[]:
        max_element=max(lst)
        index_result=lst.index(max_element)
        return index_result
    else:
        return -1

Input1=[5, 10, 15, 4, 6]
print(locate_peak(Input1))

Input2=[22 , 3, 22 , 2 , 7 , 11]
print(locate_peak(Input2))

Test_Input=[]
print(locate_peak(Test_Input))