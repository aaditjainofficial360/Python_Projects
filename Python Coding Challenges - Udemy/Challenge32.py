'''
Challenge: Flatten a List that Contains Lists (*)

Write a Python program that prints a "flattened" version of a list that contains nested lists.

"Flattened" means that all the elements in the nested lists should be added to a main list such that it doesn't contain any nested lists, just the individual.

The list could contain other elements that are not lists or other sequences, so you must check the type of each element and act appropriately.

If the list is empty, print an empty list.
'''

def flatten_list(lst):
    output=[]
    for item in lst:
        if type(item)==list:
            for elem in item:
                output.append(elem)
        else:
            output.append(item)
    return output

#Test case 1
sample1= [[1,2,3],[4,5,6],[7,8,9]]
print(flatten_list(sample1))

#Test case 2
sample2= [1,2,3,4,5,6,[7,8,9]]
print(flatten_list(sample2))

#Test case 3
sample3= [['a','b','c'],['d','e','f'],['g','h','i']]
print(flatten_list(sample3))