'''
Given the string, the task is to capitalize the first and last character of each word in a string.

Examples:

Input: hello world
Output: HellO WorlD

Input: welcome to geeksforgeeks
Output: WelcomE TO GeeksforgeekS
'''

def capitalize(string):
    capitalize_lst=[x[0].upper()+x[1:-1]+x[-1].upper() for x in string.split()]
    result = ' '.join(capitalize_lst)
    return result

print(capitalize('hello world'))

print(capitalize('welcome to geeksforgeeks'))
