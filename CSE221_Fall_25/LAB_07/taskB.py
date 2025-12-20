import sys
import heapq

n, m, s, t = map(int, sys.stdin.readline().strip().split())

graph = {}
for i in range(n):
    graph[i+1] = []

for i in range(m):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    graph[u].append((v, w))


def dijkstra(start):
    visited = {}
    distance = {}
    parent = {}

    for i in graph:
        visited[i] = 0
        distance[i] = float('inf')
        parent[i] = None

    distance[start] = 0
    parent[start] = -1

    priority_queue = [(0, start)]

    while priority_queue:
        dist, v = heapq.heappop(priority_queue)

        for x, w in graph[v]:

            if visited[x] == 0:

                if distance[x] > dist + w:
                    distance[x] = dist + w
                    parent[x] = v
                    heapq.heappush(priority_queue, (distance[x], x))

        visited[v] = 1 

    return distance


distance_alice = dijkstra(s)
distance_bob = dijkstra(t)

inf = float('inf')

smallest_time = inf
smallest_node = -1

for i in range(1, n+1):
    if distance_alice[i] != inf and distance_bob[i] != inf:
        time_required = max(distance_alice[i], distance_bob[i])

        if smallest_time > time_required:
            smallest_time = time_required
            smallest_node = i
        
        elif smallest_time == time_required:
            if smallest_node > i:
                smallest_node = i
            
            

if smallest_node == -1:
    print(-1)

else:
    print(smallest_time, smallest_node)
