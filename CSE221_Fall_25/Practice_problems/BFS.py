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


""" BFS for just graph traversal  """

# def BFS(graph, start):
#     visited = [start]
#     queue = deque([start])

#     while queue:
#         s = queue.popleft()
#         print(s)

#         for i in graph[s]:
#             if i not in visited:
#                 visited.append(i)
#                 queue.append(i)


"""  BFS for graph traversal and find out the shortedpath from every vertex to every vertex  """

# def BFS(graph, start):
    
#     visited = {}
#     distance = {}
#     parent = {}

#     for i in graph:
#         visited[i] = 0
#         distance[i] = 0
#         parent[i] = 0
    
#     visited[start] = 1
#     distance[start] = 0
#     parent[start] = -1
#     queue = deque([start])

#     while queue:
#         vertex = queue.popleft()
#         print(vertex)

#         for edge in graph[vertex]:
#             if visited[edge] == 0:
#                 visited[edge] = 1
#                 distance[edge] = distance[vertex] + 1
#                 parent[edge] = vertex
#                 queue.append(edge)

#     print(visited)
#     print(distance)
#     print(parent)


"""  BFS for shortest path from a specifc source to destination  """

def BFS(graph, start, destination):
    
    visited = {}
    parent = {}
    for i in graph:
        visited[i] = 0
        parent[i] = 0
    
    visited[start] = 1
    parent[start] = -1
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        for edge in graph[vertex]:
            if visited[edge] == 0:
                visited[edge] = 1
                parent[edge] = vertex

                if edge == destination:
                    path = compile_path(start, destination, visited, parent)
                    print(f"{start}", end = " --> ")
                    for i in path:
                        if i == destination:
                            print(i)
                        
                        else:
                            print(f"{i}", end = " --> ")

                    return 
                queue.append(edge)


def compile_path(start, destination, visited, parent):
    path = []
    while parent[destination] != -1:
        path.append(destination)
        destination = parent[destination]
    
    return path[::-1]


BFS(graph, 's', 'u')


