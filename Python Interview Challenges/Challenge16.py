'''
Write a python program to count the matching characters in a pair of string:
Examples:

Input : str1 = 'abcdef'
        str2 = 'defghia'
Output : 4
(i.e. matching characters :- a, d, e, f)

Input : str1 = 'aabcddekll12@'
        str2 = 'bb22ll@55k'
Output : 5
(i.e. matching characters :- b, 1, 2, @, k)
'''

def match_characters(string1,string2):
    set_1=set(string1)
    set_2=set(string2)
    common_set=set_1.intersection(set_2)
    return len(common_set)


#Input :
str1 = 'abcdef'
str2 = 'defghia'
print(match_characters(str1,str2))

#Input :
str1 = 'aabcddekll12@'
str2 = 'bb22ll@55k'
print(match_characters(str1,str2))
