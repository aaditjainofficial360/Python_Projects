'''
Challenge: Multiply all Elements in a List

Write a Python program that multiplies all the items in a list by the value of the variable factor.

The program must print the list as the output.

The program should also allow multiplying the variable factor by a string in case the list contains strings.

You may assume that the value of factor will be a positive integer.
'''
def multiply(lst,factor):
    result_lst=[x*factor for x in lst]
    return result_lst

#Test case 1
sample1=[3,4,5,6]
print(multiply(sample1,factor=2))

#Test case 2
sample2=['a','b','c']
print(multiply(sample2,factor=3))