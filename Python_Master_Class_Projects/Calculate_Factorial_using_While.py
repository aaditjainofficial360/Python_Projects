print('*****************FACTORIAL CALCULATOR USING WHILE LOOP*******************')
n=int(input("Enter any number: "))
product=1 
count=1
while count<=n:
    product*=count
    count+=1 
    
print()
print('Operation Completed!')
print()
print(f'Factorial of {n}: {product}')
