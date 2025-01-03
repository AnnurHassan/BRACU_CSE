import utilities


with open("input1.txt", "r") as input:
    m, n = [int(i) for i in input.readline().strip().split()]
    m += 1
    mat = []
    for i in range(m):
        mat.append([0] * m)

    for i in range(n):
        arr = [int(i) for i in input.readline().strip().split()]
        u, v, w = arr
        mat[u][v] = w
        
    utilities.print_mat(mat)
    