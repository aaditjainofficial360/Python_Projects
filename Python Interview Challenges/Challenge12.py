'''
Write a python program to find the difference between two given lists:

Examples:

Input:
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]

Output:
[10, 15, 20, 30]

Explanation:
resultant list = list1 - list2
'''

def difference_of_lists(list1,list2):
    new_lst=[x for x in list1 if x not in list2]
    return new_lst

list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]
print(difference_of_lists(list1,list2))