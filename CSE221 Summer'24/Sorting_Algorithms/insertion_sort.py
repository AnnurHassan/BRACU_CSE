import numpy as np


def print_array(array):
    for i in range(len(array)):
        print(array[i], end=" ")


def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        for j in range(i - 1, -2, -1):
            if array[j] >= temp:
                array[j + 1] = array[j]

            else:
                break

        array[j + 1] = temp

    return array


array = np.array([8, 1, 7, 6, 4, 5, 3, 2, 9])
print_array(insertion_sort(array))
