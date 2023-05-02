print('='*20)
print('Starting Level 1')
print('='*20)
'''Level 1'''
N=int(input())
#print('*'*N)

for i in range(N):
    print('*',end='')
print()
print('='*20)
print('Starting Level 2')
print('='*20)
'''Level 2'''
for i in range(N):
    for j in range(N):
        print('*',end='')
    print()