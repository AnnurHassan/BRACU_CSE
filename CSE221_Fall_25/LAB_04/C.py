import sys


n = int(sys.stdin.readline().strip())

matrix = []
for i in range(n):
    matrix.append([0]*n)

for i in range(n):
    line = list(map(int, sys.stdin.readline().strip().split()))
    for j in line[1:]:
        matrix[i][j] = 1

for i in matrix:
    for j in i:
        print(j, end = " ")
    print()
