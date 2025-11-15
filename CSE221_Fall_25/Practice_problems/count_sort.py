arr1 = [5, 7, 3, 1, 12, 4]
arr2 = [6, 8, 2, 9, 15, 0]


def count_sort(arr):

    max = float('-inf')
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]

    count_arr = [0] * (max + 1)
    for i in arr:
        count_arr[i] += 1
    
    sorted_arr = []
    for i in range(len(count_arr)):
        sorted_arr += [i] * count_arr[i]

    return sorted_arr


print(count_sort(arr1))
print(count_sort(arr2))
