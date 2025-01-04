from collections import deque
import utilities

with open("input3.txt", "r") as input:
    n, m = [int(i) for i in input.readline().strip().split()]
    graph = {}

    for i in range(n+1):
        graph[i] = []
    
    for i in range(m):
        u, v = [int(i) for i in input.readline().strip().split()]
        graph[u].append(v)
        graph[v].append(u)
    
    # utilities.print_dict(graph)

    #DFS - Recursive

    seen_list = []
    def DFS(graph, source):
        seen_list.append(source)
        u = source
        print(u, end = " ")

        for i in graph[u]:
            if i not in seen_list:
                DFS(graph, i)

    
    DFS(graph, 1)