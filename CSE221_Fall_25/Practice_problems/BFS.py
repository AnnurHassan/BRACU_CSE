graph = {'A' : ['B', 'C'], 'B' : ['D', 'E', 'F'], 'C' : ['G'], 'D' : [], 'E' : [], 'F' : ['H'], 'G' : ['I'], 'H' : [], 'I' : []}

def BFS(graph, start):
    visited = [start]
    queue = [start]

    while queue:
        s = queue.pop(0)
        print(s)

        for i in graph[s]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

BFS(graph, 'A')
