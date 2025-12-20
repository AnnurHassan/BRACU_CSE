import sys
import heapq


n, m = map(int, sys.stdin.readline().strip().split())
u = list(map(int, sys.stdin.readline().strip().split()))
v = list(map(int, sys.stdin.readline().strip().split()))
w = list(map(int, sys.stdin.readline().strip().split()))

graph = {}
for i in range(n):
    graph[i+1] = []

for i in range(m):
    parity = w[i] % 2 
    graph[u[i]].append((v[i], w[i], parity))

dist = {}
for i in range(1, n+1):
    dist[i] = [float('inf'), float('inf')] 

priority_queue = []

dist[1][0] = 0
dist[1][1] = 0
heapq.heappush(priority_queue, (0, 1, 0))
heapq.heappush(priority_queue, (0, 1, 1))

while priority_queue:
    cur_dist, u, last_parity = heapq.heappop(priority_queue)

    if cur_dist > dist[u][last_parity]:
        continue

    for v, w, parity in graph[u]:
        if parity == last_parity:
            continue 

        new_dist = cur_dist + w
        if new_dist < dist[v][parity]:
            dist[v][parity] = new_dist
            heapq.heappush(priority_queue, (new_dist, v, parity))


if min(dist[n][0], dist[n][1]) == float('inf'):
    print(-1)

else:
    print(min(dist[n][0], dist[n][1]))
