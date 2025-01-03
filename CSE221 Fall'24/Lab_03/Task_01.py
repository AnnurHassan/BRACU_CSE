def merge(a, b):
    i = 0
    j = 0
    merge_list = []

    while i < len(a) and  j < len(b):
        if a[i] <= b[j]:
            merge_list.append(a[i])
            i += 1
        
        else:
            merge_list.append(b[j])
            j += 1

    while i < len(a):
        merge_list.append(a[i])
        i += 1

    while j < len(b):
        merge_list.append(b[j])
        j += 1
    
    return merge_list


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)
    

arr = [9, 5, 4, 6, 1, 3, 2, 9]
print(mergeSort(arr))
