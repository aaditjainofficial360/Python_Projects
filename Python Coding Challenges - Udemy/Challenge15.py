'''
Challenge: Count Repeated Characters (*)

Write a Python program to count the number of repeated characters in the string s.

The program must print the total number of repeated characters and a message on the next line displaying the repeated characters separated by a space and sorted alphabetically.

If there are no repeated characters in the string, print 0 as the total count and None on the next line.
'''

def count_characters(string):
    counter=0
    repeated_char_list=list()
    for alpha in string:
        if string.count(alpha)>1 and alpha not in repeated_char_list:
            counter+=1
            repeated_char_list.append(alpha)
    repeated_char_list.sort()
    print(counter)
    result=' '.join(repeated_char_list)
    return result.strip()

#Test case 1
sample1='Hello'
print(count_characters(sample1))

#Test case 2
sample2='Coorporation'
print(count_characters(sample2))

#Test case 3
sample2='Python'
print(count_characters(sample2))