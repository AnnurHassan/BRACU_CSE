def find_max(arr):
    if len(arr) <= 1:
        return arr
    
    else:
        mid = len(arr) // 2
        left = find_max(arr[:mid])
        right = find_max(arr[mid+1:])

        if left > right:
            return left
        
        else:
            return right


arr = [5, 2, 3, 10, 1, 9]
print(find_max(arr))
