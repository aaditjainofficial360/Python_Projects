'''
Challenge: Reverse Words in a String (*)

Write a Python program that reverses the individual words in the string s and changes their capitalization. Uppercase letters should be printed in lowercase and vice versa.

Assume that the string only contains letters and spaces are used to separate words.
'''

def reverse_string(string):
    result=''
    string=string.swapcase()
    for word in string.split():
        result+=word[::-1]+' '
    return result.rstrip()

#Test case 1
sample1='Hello World'
print(reverse_string(sample1))

#Test case 2
sample2='Python is Awesome'
print(reverse_string(sample2))