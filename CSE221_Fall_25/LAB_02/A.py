import sys

 
n, k = list(map(int, sys.stdin.readline().strip().split()))
arr = list(map(int, sys.stdin.readline().strip().split()))
 
i = 0
j = n - 1
result = -1
 
while i != j:
    if arr[i] + arr[j] == k:
        result = f'{i+1} {j+1}'
        break
 
    elif arr[i] + arr[j] < k:
        i += 1
    
    elif arr[i] + arr[j] > k:
        j -= 1
 
print(result)