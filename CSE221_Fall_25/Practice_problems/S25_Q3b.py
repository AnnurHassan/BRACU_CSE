# Implementing the dividing step of the algorithm
def merge_terenary_sort(arr):
    # if len(arr) <= 1:
    #     return arr
    
    mid1 = len(arr) // 3
    mid2 = (len(arr) - mid1)
    print(arr[:mid1])
    print(arr[mid1:mid2])
    print(arr[mid2:])

    # left = merge_terenary_sort(arr[:mid1])
    # middle = merge_terenary_sort(arr[mid1:mid2])
    # right = merge_terenary_sort(arr[mid2:])

#    return merge(left, right, middle)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
merge_terenary_sort(arr)