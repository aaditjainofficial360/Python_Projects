'''
Given a String, compute all the characters, except spaces.

Input : test_str = ‘geeksforgeeks 33 best’
Output : 19
Explanation : Total characters are 19.

Input : test_str = ‘geeksforgeeks best’
Output : 17
Explanation : Total characters are 17 except spaces.
'''

def count_all(string):
    count=0
    for i in string:
        if i!=' ':
            count+=1
    return count

# Test-1
test_str1 = 'geeksforgeeks 33 best'
print(count_all(test_str1))

# Test-2
test_str2 = 'geeksforgeeks best'
print(count_all(test_str2))