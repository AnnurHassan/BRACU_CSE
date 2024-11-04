from Algorithms import bubble_sort

def main():
    with open("input2.txt", "r") as input:
        with open("output2.txt", "w") as output:
            input.readline()
            arr = [int(i) for i in input.read().strip().split(" ")]
            sorted_arr = bubble_sort(arr)
            
            for i in sorted_arr:
                output.write(f"{i} ")


if __name__ == "__main__":
    main()
