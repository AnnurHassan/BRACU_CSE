import sys


n, r = list(map(int, sys.stdin.readline().strip().split()))

graph = {}
for i in range(n):
    graph[i+1] = []

for i in range(n-1):
    u, v = list(map(int, sys.stdin.readline().strip().split()))
    graph[u].append(v)
    graph[v].append(u)

subtree_size = [0] * (n+1)
visited = [False] * (n+1)
stack = [(r, -1)] 
order = []  

while stack:
    node, parent = stack.pop()
    if node < 0:
        node = -node
        size = 1

        for child in graph[node]:
            if child != parent:
                size += subtree_size[child]

        subtree_size[node] = size
        continue

    visited[node] = True
    stack.append((-node, parent)) 
    for child in graph[node]:

        if child != parent and not visited[child]:
            stack.append((child, node))

q = int(sys.stdin.readline().strip())
for i in range(q):
    x = int(input())
    print(subtree_size[x])