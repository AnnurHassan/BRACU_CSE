graph = {'A' : ['B', 'C'], 'B' : ['D', 'E', 'F'], 'C' : ['G'], 'D' : [], 'E' : [], 'F' : ['H'], 'G' : ['I'], 'H' : [], 'I' : []}

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

DFS(graph, 'A')
