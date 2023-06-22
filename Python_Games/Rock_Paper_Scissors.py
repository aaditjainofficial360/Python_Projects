import time
print('='*50)
print('----------Welcome to famous game of Rock, Paper and Scissors----------')
print('='*50)
user1_points=0
user2_points=0
choose=input('Do you want to play this game(Yes/No): ')
while choose.lower()=='yes':
    user1=input('Enter your choice(Rock/Paper/Scissors): ')
    time.sleep(6)
    user2 = input('Enter your choice(Rock/Paper/Scissors): ')
    if user1.lower()=='rock':
        if user2.lower() not in ['paper','rock']:
            user1_points+=1
            print('You won this round !')
        elif user2.lower()=='paper':
            user2_points+=1
            print('Computer Wins this round !')
        else:
            user1_points+=1
            user2_points+=1
            print('It\'s a Tie!')

    elif user1.lower()=='paper':
        if user2.lower() not in ['paper','scissors']:
            user1_points+=1
            print('You won this round !')
        elif user2.lower()=='scissors':
            user2_points+=1
            print('Computer Wins this round !')
        else:
            user1_points+=1
            user2_points+=1
            print('It\'s a Tie!')

    else:
        if user2.lower() not in ['rock','scissors']:
            user1_points+=1
            print('You won this round !')
        elif user2.lower()=='rock':
            user2_points+=1
            print('Computer Wins this round !')
        else:
            user1_points+=1
            user2_points+=1
            print('It\'s a Tie!')
    print(f'Your Score after this round : {user1_points}')
    print(f'Computer\'s Score after this round : {user2_points}')
    choose=input('Do you want to continue playing this game(Yes/No): ')
    time.sleep(6)
print()
print('*'*20)
print('-------------SCORE SUMMARY-------------')
print(f'Your Final Score : {user1_points}')
print(f'Computer\'s Final Score : {user2_points}')
print('*'*20)
print()
print('Thank you!')

