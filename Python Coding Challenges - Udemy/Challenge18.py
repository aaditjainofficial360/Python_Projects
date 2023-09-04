'''
Challenge: Print Elements on the Same Line Without Commas

Write a Python program that prints the elements of a list on the same line.

The elements should be separated only by a space (not by a comma).

The output should not include the opening and closing square brackets [ ].
'''

def print_on_the_same_line(lst):
    result=' '.join(list(map(str,lst)))
    return result.strip()

#Test case 1
sample1=[3,4,5,6]
print(print_on_the_same_line(sample1))

#Test case 2
sample2=['a','b','c']
print(print_on_the_same_line(sample2))