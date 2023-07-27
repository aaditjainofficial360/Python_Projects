'''
Elimination Walk
Difficulty: Medium
Given a list of numbers, remove alternate elements starting from the first one. Return the list with the remaining elements. The numbers in output should be in the same order as they were in the given list. Use recursion to perform the task. Note - Don’t use loops.
Examples:
Test Case1:
Input: [1,2,3,4,5]
Output: [2,4]
Explanation: 1, 3 and 5 have been removed. Only 2, 4 remain. So, [2,4] is returned.
Test Case 2:
Input: [5,3,7,11,6,8]
Output: [3,11,8]
Explanation: 5,7 and 6 were removed. So, [3, 11, 8] is the output.
'''

def elimination_walk(lst):
    new_lst=[lst[x] for x in range(len(lst)) if not x%2==0]
    return new_lst

#Input 1
Input1 = [1,2,3,4,5]
print(elimination_walk(Input1))

#Input 2
Input2 = [5,3,7,11,6,8]
print(elimination_walk(Input2))