import sys
import math



n, q = map(int, sys.stdin.readline().strip().split())

adj = []
for i in range(n+1):
    adj.append([])

for i in range(1, n+1):

    for j in range(i+1, n+1):

        if math.gcd(i, j) == 1:
            adj[i].append(j)
            adj[j].append(i)

for i in range(q):
    x, k = map(int, sys.stdin.readline().strip().split())

    if k <= len(adj[x]):
        print(adj[x][k-1])
        
    else:
        print(-1)