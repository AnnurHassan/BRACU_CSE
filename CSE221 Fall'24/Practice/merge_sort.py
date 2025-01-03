def merge(left, right) :
    new_arr = []
    i = 0
    j = 0

    while (i < len(left) and j < len(right)):
        
        if left[i] < right[j]:
            new_arr.append(left[i])
            i += 1
        
        else:
            new_arr.append(right[j])
            j += 1
        
    while i < len(left):
        new_arr.append(left[i])
        i += 1
    
    while j < len(right):
        new_arr.append(right[j])
        j += 1
    
    return new_arr

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    else:
        mid = (len(arr) - 1) // 2

        left = arr[0: mid + 1]
        right = arr[mid + 1:]

        left_arr = merge_sort(left)
        right_arr = merge_sort(right)

    return merge(left_arr, right_arr)
    

arr = [3, 2, 5, 7, 8, 1, 0, 9, 10, 5]
print(merge_sort(arr))