'''
Given a list of integers with duplicate elements in it. The task is to generate another list, which contains only the duplicate elements. In simple words, the new list should contain elements that appear as more than one.

Examples:

Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]
Input :  list = [-1, 1, -1, 8]
Output : output_list = [-1]
'''

def duplicate(lst):
    output_lst=[]
    for i in lst:
        if lst.count(i)>1 and i not in output_lst:
            output_lst.append(i)
    return output_lst

print(duplicate([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]))

print(duplicate([-1, 1, -1, 8]))
