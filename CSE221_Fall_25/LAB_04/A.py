import sys


n, m = list(map(int, sys.stdin.readline().strip().split()))

matrix = []
for i in range(n):
    matrix.append([0]*n)

for i in range(m):
    u, v, w = list(map(int, sys.stdin.readline().strip().split()))
    matrix[u-1][v-1] = w

for i in matrix:
    for j in i:
        print(j, end = " ")
    print()
