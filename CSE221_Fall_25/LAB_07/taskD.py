import sys
import heapq

n, m, s, d = map(int, sys.stdin.readline().strip().split())
node_weight = [0] + list(map(int, input().split()))

graph = {}
for i in range(n):
    graph[i+1] = []

for i in range(m):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)

distance = {}
for i in range(1, n+1):
    distance[i] = float('inf')

distance[s] = node_weight[s]

priority_queue = [(node_weight[s], s)]

while priority_queue:
    dist, v = heapq.heappop(priority_queue)

    if dist > distance[v]:
        continue

    for x in graph[v]:
        new_dist = dist + node_weight[x]

        if new_dist < distance[x]:
            distance[x] = new_dist
            heapq.heappush(priority_queue, (new_dist, x))


if distance[d] == float('inf'):
    print(-1)

else:
    print(distance[d])
