'''
Write a python program to record the frequency of words.

Examples:
Input : test_str = 'Gfg is best'
Output : {'Gfg': 1, 'is': 1, 'best': 1}
Input : test_str = 'Gfg Gfg Gfg'
Output : {'Gfg': 3}
'''

def words_frequency(string):
    frequency_dict={}
    for i in string.split():
        frequency_dict.update({i:string.count(i)})
    return frequency_dict

# Test-case 1
test_str1 = 'Gfg is best'
print(words_frequency(test_str1))

# Test-case 2
test_str2 = 'Gfg Gfg Gfg'
print(words_frequency(test_str2))