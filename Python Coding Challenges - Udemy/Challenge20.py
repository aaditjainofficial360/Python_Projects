'''
Challenge: Check if List is Empty or Not

Write a Python program that checks if a list is empty or not.

If the list is empty, print "Empty". Else, print "Not Empty".
'''

def check_list(lst):
    if lst==[]:
        return "Empty"
    else:
        return "Not Empty"

#Test case 1
sample1=[]
print(check_list(sample1))

#Test case 2
sample2=[4]
print(check_list(sample2))

#Test case 3
sample3=[4,5,6,7]
print(check_list(sample3))