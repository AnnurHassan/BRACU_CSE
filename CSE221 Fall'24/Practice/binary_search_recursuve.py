def binary_search(arr, left, right, target):
    if left > right: 
        return -1
    
    mid = (left + right) // 2 
    
    if arr[mid] == target:  
        return mid
    
    elif arr[mid] > target: 
        return binary_search(arr, left, mid - 1, target)
    
    else: 
        return binary_search(arr, mid + 1, right, target)



arr = [0, 1, 2, 3, 5, 5, 7, 8, 9, 10]
print(binary_search(arr, 0, len(arr) - 1, 7))
