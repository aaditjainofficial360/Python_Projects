'''
Challenge: Print Common Elements in Two Lists

Write a Python program that prints a list with the elements that listA and listB have in common.

If they don't have any elements in common, print an empty list.

The program should not assume that the lists have the same length.

You may assume that each element will only appear once in each list.
'''

def common_elements(listA,listB):
    common_elements_lst=[x for x in listA if x in listB]
    return common_elements_lst

#Test case 1
sample1= [1,2,3]
sample2= [1,2,3]
print(common_elements(listA=sample1,listB=sample2))

#Test case 2
sample1= [4,5,6]
sample2= [1,4,5]
print(common_elements(listA=sample1,listB=sample2))


#Test case 3
sample1= [3,4,5]
sample2= [1,2,3]
print(common_elements(listA=sample1,listB=sample2))


#Test case 4
sample1= [4,5,6]
sample2= [1,2,3]
print(common_elements(listA=sample1,listB=sample2))