arr1 = [5, 7, 3, 1, 12, 4]
arr2 = [6, 8, 2, 9, 15, 0]

def partition(arr, start, end):

    pivot = arr[end]
    i = 0
    j = 0

    while j < end:
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

        j += 1

    arr[i], arr[end] = arr[end], arr[i]

    return i


def quick_sort(arr, start, end):
    if start >= end:
        return arr
    
    pIndex = partition(arr, start, end)
    quick_sort(arr, start, pIndex - 1)
    quick_sort(arr, pIndex + 1, end)

    return arr


print(quick_sort(arr1, 0, len(arr1) - 1))
print(quick_sort(arr2, 0, len(arr2) - 1))