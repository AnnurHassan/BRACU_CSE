import utilities
from collections import defaultdict, deque


with open("input2.txt", "r") as input:
    n, m = [int(i) for i in input.readline().strip().split()]

    # dict = defaultdict(list)

    # for i in range(m):
    #     arr = [int(i) for i in input.readline().strip().split()]
    #     u, v = arr
    #     dict[u].append((v))
    
    # utilities.print_dict(dict)

    graph = {}

    for i in range(n+1):
        graph[i] = []
    
    for i in range(m):
        arr = [int(i) for i in input.readline().strip().split()]
        u, v = arr
        graph[u].append(v)
        graph[v].append(u)

    # utilities.print_dict(graph)

    def BFS(graph, source):
        seen_list = [source]
        q = deque()
        q.append(source)

        while q:
            u = q.popleft()
            for i in graph[u]:
                if i not in seen_list:
                    seen_list.append(i)
                    q.append(i)
        
        print(seen_list)

    BFS(graph, 1)