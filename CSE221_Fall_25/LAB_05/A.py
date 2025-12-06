import sys
from collections import deque

n, m = list(map(int, sys.stdin.readline().strip().split()))

graph = {}
for i in range(n):
    graph[i+1] = []

for i in range(m):
    u, v = list(map(int, sys.stdin.readline().strip().split()))
    graph[u].append(v)
    graph[v].append(u)

visited = set([1])
queue = deque([1])

while queue:
    s = queue.popleft()
    print(s, end = " ")

    for i in graph[s]:
        if i not in visited:
            visited.add(i)
            queue.append(i)

