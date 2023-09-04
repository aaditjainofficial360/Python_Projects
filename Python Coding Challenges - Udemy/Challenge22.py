'''
Challenge: Remove Matching Element

Write a Python program that removes all occurrences of the element elem_to_remove from a list.

The output of the program should be the new list with the element removed.

If the element is not found in the list, print the message "Not Found".

If the list is empty, print "Empty List".
'''

def remove_matched_elements(lst,elem_to_remove):
    if lst!=[]:
        if elem_to_remove in lst:
            while elem_to_remove in lst:
                lst.remove(elem_to_remove)
            print(lst)
        else:
            print('Not Found')
    else:
        print('Empty List')
    return ''

#Test case 1
sample1=[1,2,3,4]
print(remove_matched_elements(sample1,elem_to_remove=2))

#Test case 2
sample2=[3,3,2,1]
print(remove_matched_elements(sample2,elem_to_remove=3))

#Test case 3
sample3=['a','b','c','b']
print(remove_matched_elements(sample3,elem_to_remove='b'))

#Test case 4
sample4=[3,4,5,6]
print(remove_matched_elements(sample4,elem_to_remove=7))

#Test case 5
sample4=[]
print(remove_matched_elements(sample4,elem_to_remove=0))
