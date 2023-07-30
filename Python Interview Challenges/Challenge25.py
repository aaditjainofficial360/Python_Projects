'''
Write a python program to filter the substrings which are greater than given length.

Examples:
Input : str = "hello geeks for geeks
          is computer science portal"
        k = 4
Output : hello geeks geeks computer
         science portal
Explanation : The output is list of all
words that are of length more than k.
Input : str = "string is fun in python"
        k = 3
Output : string python
'''

def filter_substrings_greater_than_k(string,k):
    result_string=' '.join([x for x in string.split() if len(x)>k])
    return result_string

print(filter_substrings_greater_than_k("hello geeks for geeks is computer science portal",4))

print(filter_substrings_greater_than_k("string is fun in python",3))