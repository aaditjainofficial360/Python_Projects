'''
Challenge: Print the Elements and Their Indices

Write a Python program that prints the elements of a list followed their corresponding indices.

Each element and its index must be on the same line separated by a space.

If the list is empty, print "Empty List".
'''

def printing_elements_with_indices(lst):
    if lst!=[]:
        for pos in range(len(lst)):
            print(lst[pos],pos)
    else:
        print('Empty List')
    return ''

#Test case 1
sample1=[1,2,3,4]
print(printing_elements_with_indices(sample1))

#Test case 2
sample2=['a','b','c']
print(printing_elements_with_indices(sample2))

#Test case 3
sample3=[]
print(printing_elements_with_indices(sample3))
