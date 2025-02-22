num = int(input())

for i in range(num):
    arr = input().strip().split(" ")
    if arr[2] == "+":
        print(int(arr[1]) + int(arr[3]))

    elif arr[2] == "-":
        print(int(arr[1]) - int(arr[3]))

    elif arr[2] == "/":
        print(int(arr[1]) / int(arr[3]))

    elif arr[2] == "*":
        print(int(arr[1]) * int(arr[3]))
