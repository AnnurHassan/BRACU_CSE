import sys


n, m = list(map(int, sys.stdin.readline().strip().split()))
start = list(map(int, sys.stdin.readline().strip().split()))
end = list(map(int, sys.stdin.readline().strip().split()))

dict = {}
for i in range(n):
    dict[i+1] = 0

for i in start:
    dict[i] -= 1

for i in end:
    dict[i] += 1

for values in dict.values():
    print(values, end = " ")
