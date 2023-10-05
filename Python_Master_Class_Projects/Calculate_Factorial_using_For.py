print('*****************FACTORIAL CALCULATOR USING FOR LOOP*******************')
n=int(input("Enter any number: "))
product=1 
for num in range(1,n+1):
    product*=num 
    
print()
print('Operation Completed!')
print()
print(f'Factorial of {n}: {product}')
