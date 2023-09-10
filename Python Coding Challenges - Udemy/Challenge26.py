'''
Challenge: Difference Between Two Lists

Write a Python program that prints (as a list) the elements of listA that are not in listB.

If the lists have the same elements, print an empty list.

If listA is an empty list, print an empty list.

Please assume that listA will be smaller than listB (will have fewer elements).
'''

def difference_of_lists(listA,listB):
    if listA==listB or listA==[]:
        return []
    result = [ element for element in listA if element not in listB ]
    return result

#Test case 1
sample1= [1,2,3,4]
sample2= [1,2]
print(difference_of_lists(sample1,sample2))

#Test case 2
sample1= [1,2,3,4]
sample2= [1,2,3]
print(difference_of_lists(sample1,sample2))


#Test case 3
sample1= [1,2,3,4]
sample2= [1,2,3,4]
print(difference_of_lists(sample1,sample2))


#Test case 4
sample1= []
sample2= [1,3]
print(difference_of_lists(sample1,sample2))

