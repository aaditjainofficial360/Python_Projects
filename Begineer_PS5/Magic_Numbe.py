def magical_numbe(num):
    original=num
    sum=0
    while num!=0:
        sum+=(num%10)**3
        num//=10
    if sum==original:
        return True
    else:
        return False
print(magical_numbe(153))
print(magical_numbe(124))
