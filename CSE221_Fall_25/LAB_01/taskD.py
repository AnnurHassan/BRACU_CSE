import sys


n = int(input())

for _ in range(n):
    sys.stdin.readline()
    arr = sys.stdin.readline().strip().split()
    arr = [int(i) for i in arr]
    flag = True

    for i in range(len(arr) - 1):

        if arr[i] > arr[i + 1]:
            print("NO ")
            flag = False
            break
        
    if flag:
        print("YES ")