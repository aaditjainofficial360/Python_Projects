n=int(input())
flag=True
prime_lst=[]
for num in range(2,n+1):
    for i in range(2,num):
        if num%i==0:
            flag=False
            break
    else:
        prime_lst.append(num)

print(prime_lst)    
