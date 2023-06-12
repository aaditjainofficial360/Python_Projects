import time

print('='*50)
print('Welcome to Quizpati !')
print('='*50)

choice=input('Do you want to play the game(Yes/No): ')

if choice.lower()=='yes':
    print('Be Ready for Quiz !')
    score=0
    time.sleep(4)
    q1=input('Which Team in Men\'s Category won the ICC Test Championship in Year 2023? ')
    if q1.lower()=='australia':
        print('Congrats! You are right!')
        score+=1
    else:
        print('Tough Luck!')
    time.sleep(4)
    q2=input('Which Party won  Lok Sabha elections in 2017? ')
    if q2.lower()in ['bjp','bhartiya janta party']:
        print('Congrats! You are right!')
        score+=1
    else:
        print('Tough Luck!')
    time.sleep(4)
    q3=input('Who won most WWE Championship titles in WWE history? ')
    if q3.lower()=='john cena':
        print('Congrats! You are right!')
        score+=1
    else:
        print('Tough Luck!')
    time.sleep(4)
    q4=input('Who founded Apple? ')
    if q4.lower()=='steve jobs':
        print('Congrats! You are right!')
        score+=1
    else:
        print('Tough Luck!') 
    time.sleep(4)
    q5=input('Who founded Infosys? ')
    if q5.lower()=='narayan murthy':
        print('Congrats! You are right!')
        score+=1
    else:
        print('Tough Luck!')
    time.sleep(4)
    print(f'Thank you for your valuable time!!. You have scored {score} out of 5.')
else:
    print('Thank you!')

      
    

