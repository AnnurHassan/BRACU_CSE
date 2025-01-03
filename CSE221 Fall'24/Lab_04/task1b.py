import utilities

with open("input1.txt", "r") as input:
    m, n = [int(i) for i in input.readline().strip().split()]
    m += 1

    dict = {}

    for i in range(m):
        dict[i] = []

    for i in range(n):
        arr = [int(i) for i in input.readline().strip().split()]
        u, v, w = arr
        dict[u].append((v, w))
        
    
    utilities.print_dict(dict)
