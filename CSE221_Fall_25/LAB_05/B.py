import sys
from collections import deque

n, m = list(map(int, sys.stdin.readline().strip().split()))
u = list(map(int, sys.stdin.readline().strip().split()))
v = list(map(int, sys.stdin.readline().strip().split()))

graph = {}
for i in range(n):
    graph[i+1] = []

for i in range(m):
    graph[u[i]].append(v[i])
    graph[v[i]].append(u[i])
    

visited = set()
stack = deque([1])

while stack:
    s = stack.pop()
    if s not in visited:
        print(s, end = " ")
        visited.add(s)

    for i in graph[s]:
        if i not in visited:
            stack.append(i)
