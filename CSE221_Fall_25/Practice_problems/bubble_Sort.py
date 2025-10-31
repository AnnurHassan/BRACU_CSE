import sys


def main():
    n = int(sys.stdin.readline().strip())
    arr = [int(i) for i in sys.stdin.readline().strip().split()]

    print(bubble_sort(arr))


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        sorted = True

        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                sorted = False

        if sorted:
            break

    return arr

if __name__ == "__main__":
    main()