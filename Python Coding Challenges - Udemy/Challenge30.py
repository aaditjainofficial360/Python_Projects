'''
Challenge: Find the Second Smallest Value in a List

Write a Python program that prints the second smallest value in a list.

If the list is empty or only has one element, print None.
'''

def second_smallest(lst):
    if len(lst)<2:
        return None
    return sorted(lst)[1]

#Test case 1
sample1= [1,2,3,4]
print(second_smallest(sample1))

#Test case 2
sample2= [1,3]
print(second_smallest(sample2))


#Test case 3
sample3= [2]
print(second_smallest(sample3))


#Test case 4
sample4= []
print(second_smallest(sample4))