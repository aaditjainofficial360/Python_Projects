'''
Given a String and a character K, find longest substring length of K.

Input : test_str = ‘abcaaaacbbaa’, K = b
Output : 2
Explanation : b occurs twice, 2 > 1.

Input : test_str = ‘abcaacccbbaa’, K = c
Output : 3
Explanation : Maximum times c occurs is 3.
'''

def find_longest_k(string,k):
    k_count=0
    k_max_count=0
    for i in string:
        if i==k:
            k_count+=1
            if k_count>k_max_count:
                k_max_count=k_count
        else:
            k_count=0
    return k_max_count

# Test-case 1
test_str1 = 'abcaaaacbbaa'
K = 'b'
print(find_longest_k(test_str1,k=K))

# Test-case 2
test_str2 = 'abcaacccbbaa'
K = 'c'
print(find_longest_k(test_str2,k=K))

# Test-case 3
test_str3 = 'aadit'
K = 'a'
print(find_longest_k(test_str3,k=K))