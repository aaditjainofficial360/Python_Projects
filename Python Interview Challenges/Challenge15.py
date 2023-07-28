'''
Given a List. The task is to find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of elements.

Examples:

Input: [4, 5, 1, 2, 9, 7, 10, 8]
Output:
sum =  46
average =  5.75

Input: [15, 9, 55, 41, 35, 20, 62, 49]
Output:
sum =  286
average =  35.75
'''

def calculate_sum(lst):
    return sum(lst)
def calculate_avg(lst):
    airthmetic_sum=calculate_sum(lst)
    length=len(lst)
    average=airthmetic_sum/length
    return average

list1 = [4, 5, 1, 2, 9, 7, 10, 8]
print('sum =',calculate_sum(list1))
print('average =',calculate_avg(list1))
print()
list2 = [15, 9, 55, 41, 35, 20, 62, 49]
print('sum =',calculate_sum(list2))
print('average =',calculate_avg(list2))