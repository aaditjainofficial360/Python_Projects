'''
Challenge: Distance Between Two 3D Points

Write a Python program that calculates the distance between two 3D points.

The points are represented by two lists with three elements. The first element is the x-coordinate. The second element is the y-coordinate. The third element is the z-coordinate.
'''

import math
def distance_formula(pointA,pointB):
    result=0
    for i,j in zip(pointA,pointB):
        result+=(i-j)**2
    final_output= round(math.sqrt(result),5)
    return final_output

#Test case 1
sample1= [1,2,3]
sample2= [1,2,3]
print(distance_formula(pointA=sample1,pointB=sample2))

#Test case 2
sample1= [3,4,5]
sample2= [1,3,5]
print(distance_formula(pointA=sample1,pointB=sample2))


#Test case 3
sample1= [-3,4,-5]
sample2= [2,0,-4]
print(distance_formula(pointA=sample1,pointB=sample2))