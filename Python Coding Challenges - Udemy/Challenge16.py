'''
Challenge: Sort Words in Alphabetical Order (*)

Write a Python program to convert a string s to lowercase, sort the characters of each word in alphabetical order, and print the resulting string.

You may assume that the string only contains letters and spaces to separate the words.

Spaces should be preserved in the final string.
'''

def sort_words(string):
    result=''
    string=string.lower()
    for word in string.split():
        result+=''.join(sorted(list(word)))+' '
    return result.strip()

#Test case 1
sample1='Hello World'
print(sort_words(sample1))

#Test case 2
sample2='Wonderful World'
print(sort_words(sample2))
