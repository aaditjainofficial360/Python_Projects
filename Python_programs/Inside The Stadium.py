T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for j in range(1, N + 1):
        strike_rate = sum(A[:j]) / j
        if strike_rate == 1:
            count += 1
    print(count)

'''
T=3
Input - 1
4
1 0 2 3
Result Output : 2

Input - 2
4
1 0 2 3
Result Output : 0

Input - 3
4
1 0 2 3
Result Output : 3



'''