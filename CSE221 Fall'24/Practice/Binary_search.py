def binary_Search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
    
        elif arr[mid] < target:
            left += 1
        
        else:
            right -= 1
        
    return -1


arr = [0, 1, 2, 3, 5, 5, 7, 8, 9, 10]
print(binary_Search(arr, 7))