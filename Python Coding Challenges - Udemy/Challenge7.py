'''
Challenge: Remove nth Character from a String

Write a Python program that prints the string s without the character at index n.

If the index n is out of range, print the string s intact.

If the string s is empty, print the string s intact.
'''

def missing_character(string,index):
    if index>=len(string) or string=='':
        return string
    result=string[:index]+string[index+1:]
    return result

#Test case 1
sample1='Hello'
print(missing_character(sample1,index=1))

#Test case 2
sample2='World'
print(missing_character(sample2,index=3))

#Test case 3
sample3='Dog'
print(missing_character(sample3,index=15))

#Test case 4
sample4=''
print(missing_character(sample4,index=2))
