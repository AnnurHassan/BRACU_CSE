def main():
    with open("input1b.txt", "r") as input:
        with open("output1b.txt", "w") as output:
            n = int(input.readline())

            for i in range(n):
                arr = input.readline().strip().split(" ")

                if arr[2] == "+":
                    result = int(arr[1]) + int(arr[3])
                    output.write(f"The result of {arr[1]} + {arr[3]} is {result}.\n")
                
                elif arr[2] == "-":
                    result = int(arr[1]) - int(arr[3])
                    output.write(f"The result of {arr[1]} - {arr[3]} is {result}.\n")
                
                elif arr[2] == "*":
                    result = int(arr[1]) * int(arr[3])
                    output.write(f"The result of {arr[1]} * {arr[3]} is {result}.\n")
                elif arr[2] == "/":
                    result = int(arr[1]) / int(arr[3])
                    output.write(f"The result of {arr[1]} / {arr[3]} is {result}.\n")
            


if __name__ == "__main__":
    main()