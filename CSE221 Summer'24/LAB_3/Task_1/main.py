def main():
    with open("input.txt", "r") as input:
        input.readline()

        with open("output.txt", "w") as output:
            array = list(map(int, input.readline().strip().split()))
            # array = [int(j) for i in input.readline().strip().split()]
            array = mergeSort(array)

            for i in array:
                output.write(f"{i} ")


def mergeSort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left_sub_array = array[:middle]
    right_sub_array = array[middle:]
    left_sorted = mergeSort(left_sub_array)
    right_sorted = mergeSort(right_sub_array)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    i = 0
    j = 0
    sorted_array = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1

        else:
            sorted_array.append(right[j])
            j += 1

    if i != len(left):
        sorted_array += left[i:]

    if j != len(right):
        sorted_array += right[j:]

    return sorted_array


main()
