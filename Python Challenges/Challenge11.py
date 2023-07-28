'''
Minimum Greater
Given a list of sorted integers, find in it the smallest number bigger than a given number ‘a’.
If all numbers in the given list are smaller than ‘a’, return -1.
Examples:
Test Case 1:
Input: [3,7,12,20,21,25] , 5
Output: 7
Explanation: There are many numbers in the list bigger than 5, but the smallest of them is 7.
Test Case 2:
Input: [10,20,30], 0
Output: 10
Explanation: The smallest number in the list bigger than 0 is 10.
'''

def minimum_greater(lst,num):
    for i in lst:
        if i>num:
            return i
    else:
        return -1

# Test-case 1
Input1, number1 =[3,7,12,20,21,25], 5
print(minimum_greater(Input1,number1))

# Test-case 2
Input2, number2 =[10,20,30], 0
print(minimum_greater(Input2,number2))