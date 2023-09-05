'''
Challenge: Find the Intersection of Two Sets

Write a Python program that finds the intersection of two sets (set1 and set2).

Create a new set called intersection with their intersection.

Print the new set as the output.

If the intersection is empty, print an empty set.
'''

def intersection_set(set1,set2):
    result = set1.intersection(set2)
    if len(result)>0:
        return result
    else:
        return {}

#Test case 1
set1= {1,2,3}
set2= {4,5,6}
print(intersection_set(set1,set2))

#Test case 2
set1= {1,2,3}
set2= {3,4,5}
print(intersection_set(set1,set2))

#Test case 3
set1= {1,2,3,4}
set2= {3,4,5,6}
print(intersection_set(set1,set2))

#Test case 4
set1= {1,2,3,4}
set2= {1,2,3,4}
print(intersection_set(set1,set2))
