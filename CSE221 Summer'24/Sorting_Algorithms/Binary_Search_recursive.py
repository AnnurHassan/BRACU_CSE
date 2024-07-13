def main():
    array = [10, 20, 40, 50, 60, 80 ,90, 100]
    target = 90
    print(binary_search(array, 0, len(array) -1, target))


def binary_search(array, start, end, target):
    mid = (start + end) // 2

    if start > end:
        return False

    if array[mid] == target:
        return True
    
    elif target < array[mid]:
        return binary_search(array, 0, mid - 1, target)
    
    elif target > array[mid]:
        return binary_search(array, mid + 1, end, target)



if __name__ == "__main__":
    main()