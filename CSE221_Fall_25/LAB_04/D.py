import sys


n, m = list(map(int, sys.stdin.readline().strip().split()))
u = list(map(int, sys.stdin.readline().strip().split()))
v = list(map(int, sys.stdin.readline().strip().split()))

graph = {}
for i in range(n):
    graph[i+1] = []

for i in range(m):
    graph[u[i]].append(v[i])
    graph[v[i]].append(u[i])

deg = [0] * (n+1)
for node, edges in graph.items():
    deg[node] += len(edges)

odd_count = 0
for i in range(1, len(deg)):
    if deg[i] % 2 != 0:
        odd_count += 1

if odd_count == 0 or odd_count == 2:
    print('YES')

else:
    print('NO')