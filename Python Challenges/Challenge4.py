'''
Tail match
Difficulty: Hard
Question: Given a list of integers, group all numbers which end with the same digit and return as a dictionary. The keys of the dictionary will be the last digit and value of dictionary will be a list of numbers. If given list is empty return -1.
Examples:
Test Case 1:
Input - [5, 10, 15, 4, 50]
Output - {5: [5,15], 0: [10, 50], 4: [4]}
Explanation - 5 and 15 end with 5, so they are grouped together. 10 and 50 end with 0. 4 ends with 4.
Test Case 2:
Input - [22,3,22,2,71,11]
Output - {2: [22, 22, 2], 3: [3], 1: [71, 11]}
Explanation - 22, 22 and 2 end with 2, so they are grouped together. 3 ends with 3. 71 and 11 end with 1.
'''

def tail_match(lst):
    if lst!=[]:
        result={}
        for i in lst:
            if int(str(i)[-1]) not in result:
                result.update({int(str(i)[-1]):[i]})
            else:
                result[int(str(i)[-1])].append(i)
        return result
    else:
        return -1

Input1=[5, 10, 15, 4, 50]
print(tail_match(Input1))

Input2=[22, 3, 22, 2, 71, 11]
print(tail_match(Input2))

Test_Input=[]
print(tail_match(Test_Input))