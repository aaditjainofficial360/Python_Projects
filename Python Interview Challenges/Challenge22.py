'''
Write a python program to extract all tuple pair combinations from the pair of tuple:

Examples :

Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]

Input : test_tuple1 = (9, 2), test_tuple2 = (7, 8)
Output : [(9, 7), (9, 8), (2, 7), (2, 8), (7, 9), (7, 2), (8, 9), (8, 2)]
'''

def extract_tuple_combinations(tuple1,tuple2):
    output_lst=[]
    for i in tuple1:
        for j in tuple2:
            output_lst.append((i,j))
    for i in tuple2:
        for j in tuple1:
            output_lst.append((i,j))
    return output_lst

# Input 1
print(extract_tuple_combinations(tuple1 = (7, 2),tuple2 = (7, 8)))

# Input 2
print(extract_tuple_combinations(tuple1 = (9, 2), tuple2 = (7, 8)))
