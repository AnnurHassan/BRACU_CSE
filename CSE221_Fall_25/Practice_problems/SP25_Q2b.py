arr = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

def binary_Search(arr):
    
    l = 0
    h = len(arr)

    while l < h:
        mid = (l + h) // 2

        if arr[mid] == 1:
            if arr[mid - 1] == 0:
                return mid

            else:
                h = mid - 1
        
        else:
            if arr[mid + 1] == 1:
                return mid + 1
            
            else:
                l = mid + 1
            
            

print(binary_Search(arr))    