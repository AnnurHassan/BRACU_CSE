import numpy as np


def print_array(array):
    for i in range(len(array)):
        print(array[i], end=" ")


def bubble_sort(array):
    n = 0
    flag = True
    for i in range(len(array)):
        n += 1
        for j in range(1, len(array)):
            n += 1
            if array[j] <= array[j - 1]:
                temp = array[j - 1]
                array[j - 1] = array[j]
                array[j] = temp
                flag = False

        if flag:
            return array

    return array


array = np.array([7, 2])
bubble_sort(array)
print_array(bubble_sort(array))
