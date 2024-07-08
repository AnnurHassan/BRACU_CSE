def merge_sort(items):
    if len(items) <= 1:
        return items

    middle_index = len(items) // 2              # Finding the mdidle index
    left_split = items[:middle_index]           # split using the middle index
    right_split = items[middle_index:]          # split using the middle index
    left_sorted = merge_sort(left_split)        # calling merge sort recursievly on left array
    right_sorted = merge_sort(right_split)      # calling merge sort recursievly on right array

    return merge(left_sorted, right_sorted)     # merging the left and right array


def merge(left, right):                         # merge fuction for merging the left array
    result = []                                 # to store the sorted array
    i = 0
    j = 0
    while i < len(left) and j < len(right):                      
        if left[i] < right[j]:                  # checking to see which on is smallest
            result.append(left[i])              # appending the smallest value to the sorted array
            i += 1                              # removing the first element 
        else:
            result.append(right[j])
            j += 1
    
    if i != len(left):                          # adding the remaining elements to the sorted array
        result = result + left[i:]
    
    if j != len(right):
        result = result + right[j:]


    return result


print(merge_sort([1, 4, 3, 2, 5, 6]))
