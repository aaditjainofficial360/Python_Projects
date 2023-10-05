print('*****************FACTORS FETCHER*******************')
n=int(input("Enter any number: "))
factors_lst=[]
for fac in range(1,n+1):
    if n%fac==0:
        factors_lst.append(fac)
print()
print('Operation Completed!')
print()
print(f'Here are the factors of {n} : {factors_lst}')
