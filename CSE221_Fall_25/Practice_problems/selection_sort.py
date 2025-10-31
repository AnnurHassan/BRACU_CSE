import sys


def main():
    arr = [int(i) for i in sys.stdin.readline().strip().split()]

    print(selection_sort(arr))


def selection_sort(arr):
    count = 0
    for i in range(len(arr)):
        min = i
        
        for j in range(i, len(arr)):
            if arr[j] < arr[min]:
                min = j
        
        if min != i:
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp
            count += 1
        
    return arr, count


if __name__ == "__main__":
    main()