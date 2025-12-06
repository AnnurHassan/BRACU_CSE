import sys
from collections import deque


n, m, s, d, k = list(map(int, sys.stdin.readline().strip().split()))

graph = [[] for i in range(n+1)]
for i in range(m):
    u, v = list(map(int, sys.stdin.readline().strip().split()))
    graph[u].append(v)


visited = [False] * (n+1)
parent = [-1] * (n+1)

visited[s] = True
queue = deque([s])

while queue:
    node = queue.popleft()
    for nei in graph[node]:
        if not visited[nei]:
            visited[nei] = True
            parent[nei] = node
            queue.append(nei)


if parent[k] == -1 and s != k:
    print(-1)
    sys.exit()


path1 = []
cur = k
while cur != -1:
    path1.append(cur)
    cur = parent[cur]
path1.reverse()


visited = [False] * (n+1)
parent = [-1] * (n+1)

visited[k] = True
queue = deque([k])

while queue:
    node = queue.popleft()
    for nei in graph[node]:
        if not visited[nei]:
            visited[nei] = True
            parent[nei] = node
            queue.append(nei)


if parent[d] == -1 and k != d:
    print(-1)
    sys.exit()

path2 = []
cur = d
while cur != -1:
    path2.append(cur)
    cur = parent[cur]
path2.reverse()


full_path = path1 + path2[1:]

print(len(full_path)-1)
print(*full_path)
