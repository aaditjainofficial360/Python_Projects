num=int(input("Enter an45y number: "))
count=0
while num!=0:
    if num%2==0:
        num//=2
    else:
        num-=1
    count+=1
print(f"It tool {count} steps to the entered number to reduce to zero.")
        