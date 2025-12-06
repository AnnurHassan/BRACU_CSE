import sys


n, m = list(map(int, sys.stdin.readline().strip().split()))
u = list(map(int, sys.stdin.readline().strip().split()))
v = list(map(int, sys.stdin.readline().strip().split()))
w = list(map(int, sys.stdin.readline().strip().split()))

dict = {}

for i in range(0, n):
    dict[i+1] = []

for i in range(m):
    dict[u[i]].append((v[i], w[i]))

for key, value in dict.items():
    print(f"{key} : ", end = "")

    for i in value:
        print(i, end = " ")

    print()