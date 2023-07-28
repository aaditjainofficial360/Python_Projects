'''
Given a list of tuples, write a Python program to sort the tuples by the second item of each tuple.

Examples:

Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)]
Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]

Input : [('452', 10), ('256', 5), ('100', 20), ('135', 15)]
Output : [('256', 5), ('452', 10), ('135', 15), ('100', 20)]
'''

def sort_by_second_item(lst):
    output_lst=[]
    num_lst=[]
    for i in lst:
        num_lst.append(i[1])
    num_lst.sort()
    for j in num_lst:
        for k in lst:
            if j==k[1]:
                output_lst.append(k)
    return output_lst


print(sort_by_second_item([('for', 24), ('Geeks', 8), ('Geeks', 30)]))

print(sort_by_second_item([('452', 10), ('256', 5), ('100', 20), ('135', 15)]))