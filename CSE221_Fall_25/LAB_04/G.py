import sys


n, m, k = list(map(int, sys.stdin.readline().strip().split()))
knights = set()
for i in range(k):
    x, y = list(map(int, sys.stdin.readline().strip().split()))
    knights.add((x, y))

for x, y in knights:
    if (x+2, y+1) in knights:
        print('YES')
        exit()

    if (x+2, y-1) in knights:
        print('YES')
        exit()

    if (x-2, y+1) in knights:
        print('YES')
        exit()

    if (x-2, y-1) in knights:
        print('YES')
        exit()

    if (x+1, y+2) in knights:
        print('YES')
        exit()
    
    if (x+1, y-2) in knights:
        print('YES')
        exit()
    
    if (x-1, y+2) in knights:
        print('YES')
        exit()
    
    if (x-1, y-2) in knights:
        print('YES')
        exit()

print('NO')



