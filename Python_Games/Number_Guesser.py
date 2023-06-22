import random

print('*'*50)
print('----Welcome to Guessing Game----')
print('*'*50)
start=int(input('Enter the starting value: '))
end=int(input('Enter the ending value: '))
if start<=end:
    num=int(input(f'Enter any number between {start} and {end}: '))
    random_num=random.randint(start,end)
    if random_num==num:
        print('You have rightly guessed! Congratulations!')
    else:
        print('Bad Luck!')
else:
    print('Starting value should be lesser than ending value')