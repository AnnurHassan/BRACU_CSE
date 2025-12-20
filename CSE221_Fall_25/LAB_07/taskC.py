import sys
import heapq



n, m = map(int, sys.stdin.readline().strip().split())

graph = {}
for i in range(n):
    graph[i+1] = []

for i in range(m):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

danger = {}
for i in range(1, n+1):
    danger[i] = float('inf')

danger[1] = 0
priority_queue = [(0, 1)]

while priority_queue:
    current_danger, v = heapq.heappop(priority_queue)

    if current_danger > danger[v]:
        continue

    for x, w in graph[v]:
        new_danger = max(current_danger, w)

        if new_danger < danger[x]:
            danger[x] = new_danger
            heapq.heappush(priority_queue, (new_danger, x))


for i in range(1, n + 1):
    if danger[i] == float('inf'):
        print(-1, end = " ")
    else:
        print(danger[i], end = " ")

