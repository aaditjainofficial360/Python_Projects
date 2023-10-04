print('*****************FIBONACCI SERIES USING FOR LOOP*******************')
n=int(input("Enter the no. of terms : "))
fibonacci_lst=[]
if n==1:
    fibonacci_lst.append(0)
elif n==2:
    fibonacci_lst.extend([0,1])
else:
    fibonacci_lst.extend([0,1])
    for no_of_times in range(n-2):
        fibonacci_lst.append(fibonacci_lst[-1]+fibonacci_lst[-2])
print()
print('Operation Completed!')
print()
print(f'Your Fibonacci series are as follows :{fibonacci_lst}')
