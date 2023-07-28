'''
Given a String, perform uppercase of the later part of the string.

Input : test_str = 'geeksforgeek'
Output : geeksfORGEEK
Explanation : Latter half of string is uppercased.
Input : test_str = 'apples'
Output : appLES
Explanation : Latter half of string is uppercased.
'''

def paint_laterhalf(string):
    length=len(string)
    result=string[:length//2]+string[length//2:].upper()
    return result

# Test-case 1
test_str1 = 'geeksforgeek'
print(paint_laterhalf(test_str1))

# Test-case 2
test_str2 = 'apples'
print(paint_laterhalf(test_str2))
