import sys


n = int(sys.stdin.readline().strip())
arr = [int(i) for i in sys.stdin.readline().strip().split()]

count = 0

for i in range(n):
    min = i

    for j in range(i, n):
        if arr[j] < arr[min]:
            min = j
        
    if min != i:
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
        count += 1

print(arr, count)