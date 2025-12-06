import sys
from collections import deque


n, m, s, d = list(map(int, sys.stdin.readline().strip().split()))
u = list(map(int, sys.stdin.readline().strip().split()))
v = list(map(int, sys.stdin.readline().strip().split()))

graph = [[] for i in range(n+1)]
for i in range(m):
    graph[u[i]].append(v[i])
    graph[v[i]].append(u[i])

for i in range(1, n+1):
    graph[i].sort()

visited = [False] * (n+1)
parent = [-1] * (n+1)

visited[s] = True
queue = deque([s])

while queue:
    s = queue.popleft()

    if s == d:
        break

    for i in graph[s]:
        if not visited[i]:
            visited[i] = True
            parent[i] = s
            queue.append(i)

if parent[d] == -1 and s != d:
    print(-1)
    exit()


path = []
cur = d
while cur != -1:
    path.append(cur)
    cur = parent[cur]

path.reverse()


print(len(path)-1)
print(*path)
