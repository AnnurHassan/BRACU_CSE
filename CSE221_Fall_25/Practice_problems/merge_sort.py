arr1 = [5, 7, 3, 1, 12, 4]
arr2 = [6, 8, 2, 9, 15, 0]


def merge(left, right):
    arr = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        
        else:
            arr.append(right[j])
            j += 1
        
    if i != len(left):
        arr += left[i:]
    
    if j != len(right):
        arr += right[j:]

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


print(merge_sort(arr1))
print(merge_sort(arr2))