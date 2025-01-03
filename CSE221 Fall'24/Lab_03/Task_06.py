def partition(arr, low, high):
    pivot = arr[high]
    wall = low - 1
    for i in range(low, high + 1):
        if arr[i] <= pivot:
            wall += 1

            if wall != i:
                arr[wall], arr[i] = arr[i], arr[wall]
    
    return wall


def quicksort(arr, low, high, k):
    if low == high:
        return arr[low]
    
    pivot = partition(arr, low, high)
    k_th = k - 1
    if pivot == k_th:
        return arr[pivot]

    elif pivot > k_th:
        return quicksort(arr, low, pivot - 1, k)

    else:
        quicksort(arr, pivot + 1, high, k)

arr = [9, 5, 4, 6, 1, 3, 2, 9]
print(quicksort(arr, 0, (len(arr) - 1), 5))