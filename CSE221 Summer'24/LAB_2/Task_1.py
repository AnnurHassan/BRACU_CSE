def main():
    with open("input1.txt", "r") as input:
        
        with open("ouput1.txt", "w") as output:
            sum = int((input.readline().split())[1])
            array = input.readline().split()

            for i in range(len(array)):
                j = len(array) - 1

                if int(array[i]) + int(array[j]) == sum:
                    output.write(f"{i+1} {j+1}")
                    return

                elif int(array[i]) + int(array[j]) < sum:
                    j -= 1

                if i == j:
                    output.write("IMPOSSIBLE")

main()