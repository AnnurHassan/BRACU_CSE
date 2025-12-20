import heapq
import sys 


n, m, s, d = list(map(int, sys.stdin.readline().strip().split()))
u = list(map(int, sys.stdin.readline().strip().split()))
v = list(map(int, sys.stdin.readline().strip().split()))
w = list(map(int, sys.stdin.readline().strip().split()))


graph = {}

for i in range(n):
    graph[i+1] = []

for i in range(len(u)):
    graph[u[i]].append((v[i], w[i]))

visited = {}
distance = {}
parent = {}

for i in graph:
    visited[i] = 0
    distance[i] = float('inf')
    parent[i] = None

distance[s] = 0
parent[s] = -1

priority_queue = [(0, s)]

while priority_queue:
    dist, v = heapq.heappop(priority_queue)

    for x, w in graph[v]:
        if visited[x] == 0:
            if distance[x] > dist + w:
                distance[x] = dist + w
                parent[x] = v
                heapq.heappush(priority_queue, (distance[x], x))
    visited[v] = 1 
  
if distance[d] == float('inf'):
    print(-1)

else:
    print(distance[d])
    path = []
    current_node = d
    while current_node != -1:
        path.append(current_node)
        current_node = parent[current_node]

    for i in path[::-1]:
        print(i, end = " ")