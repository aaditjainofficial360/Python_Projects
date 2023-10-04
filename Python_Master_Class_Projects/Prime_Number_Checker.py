print('*****************PRIME NUMBER CHECKER*******************')
n=int(input("Enter any number: "))
flag=True
for i in range(2,n):
    if n%i==0:
        flag=False
        break
    
if flag:
    print('It is Prime!')
else:
    print('It is not Prime!')
