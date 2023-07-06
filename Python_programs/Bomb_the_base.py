T=int(input())
for i in range(T):
    N,X=map(int,input().split())
    houses_defence=list(map(int,input().split()))
    total_houses=N
    bomb_strength=X
    houses_affected=0
    for i in range(total_houses):
        if houses_defence[i]<bomb_strength:
            houses_affected=len(houses_defence[:i+1])
    print(houses_affected)

'''
T=2
Input- 1 
8 6
4 1 6 1 6 5 6 8
Result Output : 6

Input- 2
2 1
3 5
Result Output : 0
'''