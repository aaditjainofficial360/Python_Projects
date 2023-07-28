'''
Write a python program to extract digits from tuple list:

Examples:

Input : test_list = [(15, 3), (3, 9)]
Output : [9, 5, 3, 1]

Input : test_list = [(15, 3)]
Output : [5, 3, 1]
'''

def extract_numbers(lst):
    output_lst=[]
    for i in lst:
        for j in i:
            if j not in output_lst:
                if j<10:
                    output_lst.append(j)
                else:
                    for k in str(j):
                        output_lst.append(int(k))
            else:
                continue
    return output_lst

# Test-case 1
test_list1 = [(15, 3), (3, 9)]
print(extract_numbers(test_list1))

# Test-case 2
test_list2 = [(15, 3)]
print(extract_numbers(test_list2))