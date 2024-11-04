def main():
    with open("input1a.txt", "r") as input:
        with open("output1a.txt", "w") as output:
            n = int(input.readline())
            
            for i in range(n):
                val = int(input.readline())

                if val % 2 == 0:
                    output.write(f"{val} is an even Number.\n")
                
                else:
                    output.write(f"{val} is a odd Number.\n")


if __name__ == "__main__":
    main()