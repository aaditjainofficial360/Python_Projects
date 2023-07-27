'''
Over here
Difficulty: Easy
Given a list of integers, find a number in it which satisfies the equation x2 - 14x + 40. If none of the numbers satisfy, return -1.
Examples:
Test Case 1:
Input: [3,2,1,4,6,8]
Output: 4
Explanation: If we put 4 in the equation, we get 4^2 - 14*4 + 40 = 16 - 56 + 40 = 0. So, 4 satisfies the equation.
Test Case 2:
Input: [100,20,30,40,50]
Output: -1
Explanation: None of the numbers in the list satisfy the equation, so we return -1.
'''

def over_here(lst):
    def equation(x):
        result=x**2-14*x+40
        return result
    for i in lst:
        if equation(i)==0:
            return i
    else:
        return -1
#Test-case 1
Input1 = [3,2,1,4,6,8]
print(over_here(Input1))

#Test-case 2
Input2 = [100,20,30,40,50]
print(over_here(Input2))
