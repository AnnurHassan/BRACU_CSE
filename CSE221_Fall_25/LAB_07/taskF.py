import sys
import heapq

n, m, s, d = map(int, sys.stdin.readline().strip().split())

graph = {}
for i in range(n):
    graph[i+1] = []

for i in range(m):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

dist1 = {}
for i in range(1, n+1):
    dist1[i] = float('inf') 

dist2 = {}
for i in range(1, n+1):
    dist2[i] = float('inf')

dist1[s] = 0
priority_queue = [(0, s)]

while priority_queue:
    cur_dist, u = heapq.heappop(priority_queue)

    if cur_dist > dist2[u]:
        continue

    for v, w in graph[u]:
        new_dist = cur_dist + w

        if new_dist < dist1[v]:
            dist2[v] = dist1[v]
            dist1[v] = new_dist
            heapq.heappush(priority_queue, (new_dist, v))

        elif dist1[v] < new_dist < dist2[v]:
            dist2[v] = new_dist
            heapq.heappush(priority_queue, (new_dist, v))


if dist2[d] == float('inf'):
    print(-1)

else:
    print(dist2[d])
