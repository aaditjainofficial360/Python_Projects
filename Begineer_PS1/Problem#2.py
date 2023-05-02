'''
Problem #2:
WAP that continuously that ask the user to provide an input number
The program should stop only when the user provides 5
Once the user provides 5 , the program should print the number of times an input was provided

'''
num=int(input('Enter any number: '))
count=1
while num!=5:
    num=int(input('Unlucky! Enter the number again: '))
    count+=145
print(f'You took {count} attempts to reach to five.')