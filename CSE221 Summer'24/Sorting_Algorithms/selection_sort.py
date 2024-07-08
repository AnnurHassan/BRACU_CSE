import numpy as np


def print_array(array):
    for i in range(len(array)):
        print(array[i], end=" ")


def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i, len(array)):
            if array[min] >= array[j]:
                min = j

        temp = array[i]
        array[i] = array[min]
        array[min] = temp

    return array


array = np.array([5, 8, 7, 6, 4, 1, 3, 2, 9])
print_array(selection_sort(array))
