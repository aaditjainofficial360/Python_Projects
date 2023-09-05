'''
Challenge: Count Elements Greater than 3

Write a Python program that counts the number of elements in a list with value greater than 3.

You may assume that the list only contains numbers.

Print the final count.
'''

def count_elements_greater_than_3(lst):
    counter=0
    for element in lst:
        if element>3:
            counter+=1
    return counter

#Test case 1
sample1=[1,-1,0,2,2,3]
print(count_elements_greater_than_3(sample1))

#Test case 2
sample2=[1,2,3,4]
print(count_elements_greater_than_3(sample2))

#Test case 3
sample3=[7,8,9,10]
print(count_elements_greater_than_3(sample3))

#Test case 4
sample4=[]
print(count_elements_greater_than_3(sample4))