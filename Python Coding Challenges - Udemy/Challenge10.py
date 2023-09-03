'''
Challenge: Check if String Contains All Letters in the Alphabet

Write a Python program that checks if the string s contains all the letters in the alphabet (case-insensitive, so "A" should be equivalent to "a").

If it does, print True. Else, print False.

Before comparing the characters, you should convert the string to lowercase.

If the string contains spaces, ignore them before finding the result.

You may assume that the string doesn't contain any other symbols, only spaces (possibly).

Consider these letters as part of the alphabet: 'abcdefghijklmnopqrstuvwxyz'
'''

def check_string(string):
    alphabets_sum=sum([x for x in range(97,123)])
    if ' ' in string:
        string_sum=sum([ord(y) for y in string])
    else:
        string_sum=sum([ord(alpha) for y in string.split() for alpha in y])
    if string_sum>=alphabets_sum:
        return True
    return False

#Test case 1
sample1='abcdefghijklmnopqrstuvwxyz'
print(check_string(sample1))

#Test case 2
sample2='The quick brown fox jumps over the lazy dog'
print(check_string(sample2))

#Test case 2
sample3='Hello'
print(check_string(sample3))