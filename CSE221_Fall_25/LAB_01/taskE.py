def bubbleSort(arr):                                                    
    for i in range(len(arr)-1):
        sorted = True
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sorted = False

        if sorted:
            break

n = int(input())
arr = [int(i) for i in input().split()]
bubbleSort(arr)
for i in arr:
    print(int(i), end=' ')