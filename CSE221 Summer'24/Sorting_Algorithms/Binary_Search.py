def main():
    array = [10, 20, 40, 50, 60, 80 ,90, 100]
    target = 900
    print(binary_search(array, target))


def binary_search(array, target):
    i = 0
    j = len(array) - 1

    while (i <= j):
        middle = (i + j) // 2
        
        if array[middle] == target:
            return True

        elif target < array[middle]:
            j = middle - 1
        
        elif target > array[middle]:
            i = middle + 1
    
    return False

    

if __name__ == "__main__":
    main()