'''
Challenge: Get Max and Min Values

Write a Python program that prints the largest and smallest values in a list

Print the two values on the same line, separated by a space.

The largest value should appear first and the smallest value should appear second.

You may assume that the list only contains numeric values.

If the list is empty, print None.
'''

def get_max_min(lst):
    if lst==[]:
        return None
    print(max(lst),min(lst))
    return ''

#Test case 1
sample1=[3,4,5,6]
print(get_max_min(sample1))

#Test case 2
sample2=[-1,-2,-3,-4]
print(get_max_min(sample2))

#Test case 3
sample3=[0,0,0,0]
print(get_max_min(sample3))

#Test case 4
sample4=[]
print(get_max_min(sample4))