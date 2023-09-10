'''
Challenge: Find the Second Largest Value in a List

Write a Python program that prints the second largest value in a list.

If the list is empty or only has one element, print None.
'''

def second_largest(lst):
    if lst==[] or len(lst)==1:
        return None
    return sorted(lst)[-2]

#Test case 1
sample1= [1,2,3,4]
print(second_largest(sample1))

#Test case 2
sample2= [1,2]
print(second_largest(sample2))


#Test case 3
sample3= [2]
print(second_largest(sample3))


#Test case 4
sample4= []
print(second_largest(sample4))