'''
Given two strings s1 and s2. The task is to find out the minimum number of string rotations for the given string s1 to obtain the actual string s2. Examples:

Input : eeksg, geeks
Output: 1
Explanation: g is rotated left to obtain geeks.

Input : eksge, geeks
Output: 2
Explanation : e and g are left rotated to obtain geeks.
'''

def rotate(string1,string2):
    no_of_rotations=0
    while string1!=string2:
        string1=string1[-1]+string1[:-1]
        no_of_rotations+=1
    return no_of_rotations

print(rotate('eeksg', 'geeks'))

print(rotate('eksge', 'geeks'))