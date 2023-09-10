'''
Challenge: Make a Frequency Dictionary from the Elements of a List (*)

Write a Python program that creates and print a dictionary that maps each element in a list to its corresponding frequency (how many times it occurs in the list).

The test should be case-sensitive. Therefore, "A" should not be considered the same element as "a".
'''

def frequency_dictionary(lst):
    output={}
    for elem in lst:
        output[elem]=lst.count(elem)
    return output

#Test case 1
sample1= ['a','a','b','c','a','b']
print(frequency_dictionary(sample1))

#Test case 2
sample2= [1,2,3,4,3,2,1,2]
print(frequency_dictionary(sample2))