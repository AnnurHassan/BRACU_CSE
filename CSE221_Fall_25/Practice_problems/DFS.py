from collections import deque


graph = {
        'r' : ['v', 's'], 
        's' : ['w', 'r'], 
        't' : ['w', 'x', 'u'], 
        'u' : ['t', 'y'], 
        'v' : ['r'], 
        'w' : ['s', 't', 'x'], 
        'x' : ['w', 't', 'y'], 
        'y' : ['u', 'x'] 
}


def DFS(graph, start):
    visited = [start]
    stack = [start]

    while stack:
        s = stack.pop()
        print(s)

        for i in graph[s]:
            if i not in visited:
                visited.append(i)
                stack.append(i)

DFS(graph, 's')
