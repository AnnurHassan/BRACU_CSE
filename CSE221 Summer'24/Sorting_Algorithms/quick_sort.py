def partition(list, start, end):

    pivot = list[end]                  # setting pivot index to the last element's index 
    less_than_pivot = start            # keeping track of index of the elements that are smaller than pivot element
    for i in range(start, end):        # looping from start to end
        if list[i] < pivot:            # checking if smaller than pivot element
            list[i], list[less_than_pivot] = list[less_than_pivot], list[i]  # swapping with elemets in place 
            less_than_pivot += 1       # incrementing index of the elements that are smaller than pivot element
        
    list[end], list[less_than_pivot] = list[less_than_pivot], list[end]  # swapping the pivot element to its place

    return less_than_pivot             # return the pivot index


def quicksort(list, start, end):                                
    if start >= end:                   # if the list is of length 1 or 0: terminate function
        return                                                                      

    pivot = partition(list, start, end)  # getting the pivot index
    quicksort(list, start, pivot - 1)    # calling recursively on the left sublist
    quicksort(list, pivot + 1, end)      # calling recursively on the right sublist                    


array = [5, 8, 6, 2, 1, 3, 4, 7]
quicksort(array, 0, len(array) - 1)
print(array)

array = [1, 20, 5, 70, 15, 13, 100, 30, 50, 60, 25, 16]
quicksort(array, 0, len(array) - 1)
print(array)
