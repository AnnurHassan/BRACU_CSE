def partition(arr, low, high):
    pivot = arr[high]
    wall = low - 1
    for i in range(low, high + 1):
        if arr[i] <= pivot:
            wall += 1

            if wall != i:
                arr[wall], arr[i] = arr[i], arr[wall]
    
    return wall


def quicksort(arr, low, high):
    if low < high:
        wall = partition(arr, low , high)
        quicksort(arr, low, wall - 1)
        quicksort(arr, wall + 1, high)

arr = [9, 5, 4, 6, 1, 3, 2, 9]
quicksort(arr, 0, len(arr) - 1)
print(arr)