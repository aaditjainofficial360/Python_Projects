'''
Kaprekarian riddles
Difficulty: Medium
Question: Kaprekar numbers are a special kind of numbers whose repeated sum of digits always add up to either 1 or 9. For example:
6174
=> 6 + 1 + 7 + 4 = 18
=> 1 + 8 = 9
As you can see, this was done in two steps.
Your task is to complete the function with the definition solve_kaprekar(number: int, max_steps: int), which returns whether the function comes out to be a Kaprekar Number within the number of steps less than or equal to max_steps, and return either True or False.
Examples:
Test Case 1:
Input: number=1, max_steps=3
Output: True
Explanation: 1 is a Kaprekar number since the sum of its digits is 1. So we return True
Test Case 2:
Input: number=1674, max_steps=1
Output: False
Explanation: 1+6+7+4 = 18 (Step 1)
1 step has been completed, and the sum of digits hasn’t been 1 or 9. So we stop execution here, and return False
Test Case 3:
Input: number=93, max_steps=4
Output: False
Explanation: 9+3=12 (Step 1), 1+2 = 3 (Step 2)
We can’t move anymore since the sum is a single digit number now. So we return False
'''

def solve_kaprekar(number, max_steps):
    sum=0
    steps=0
    if number not in (1, 9):
        while True:
            sum+=number%10
            number//=10
            if number==0:
                steps+=1
                number=sum
                sum=0
            if steps>max_steps:
                return False
    else:
        return True

print(solve_kaprekar(1,3))
print(solve_kaprekar(1674,1))
print(solve_kaprekar(93,4))
