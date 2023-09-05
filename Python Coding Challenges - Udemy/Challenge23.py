'''
Challenge: Remove Duplicates from a List

Write a Python program that removes duplicate elements from a list, only keeping one occurrence of each element in the list.

The original list should be mutated (modified).

The program must print the final version of the list.
'''

def remove_duplicates(lst):
    result=[]
    if lst==[]:
        return []
    else:
        for element in lst:
            if element not in result:
                result.append(element)
        return result

#Test case 1
sample1=[1,1,2,3,4,4]
print(remove_duplicates(sample1))

#Test case 2
sample2=['a','a','b','a']
print(remove_duplicates(sample2))

#Test case 3
sample3=[1,2,3]
print(remove_duplicates(sample3))

#Test case 4
sample4=[]
print(remove_duplicates(sample4))