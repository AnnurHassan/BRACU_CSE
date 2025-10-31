import sys


n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

for i in range(n):

    for j in range(n - 1):

        if arr[j] > arr[j + 1]:

            if arr[j] % 2 == 0 and arr[j+1] % 2 == 0:
                arr[j], arr[j + 1] = arr[j+1], arr[j]
             
            elif arr[j] % 2 != 0 and arr[j+1] % 2 != 0:
                arr[j], arr[j + 1] = arr[j+1], arr[j]

for i in arr:
    print(i, end=" ")
print()