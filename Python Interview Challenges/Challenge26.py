'''
Given a string S, containing numeric words, the task is to convert the given string to the actual number.

Example:

Input: S = “zero four zero one”
Output: 0401

Input: S = “four zero one four”
Output: 4014
'''

def words_to_numbers(string):
    num_string=''
    for i in string.split():
        if i=='one':
            num_string+='1'
        elif i=='two':
            num_string+='2'
        elif i=='three':
            num_string+='3'
        elif i=='four':
            num_string+='4'
        elif i=='five':
            num_string+='5'
        elif i=='six':
            num_string+='6'
        elif i=='seven':
            num_string+='7'
        elif i=='eight':
            num_string+='8'
        elif i=='nine':
            num_string+='9'
        elif i=='zero':
            num_string+='0'
    return num_string

print(words_to_numbers("zero four zero one"))

print(words_to_numbers("four zero one four"))