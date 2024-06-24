def main():
    with open("input.txt", "r") as input:
        input.readline()

        with open("ouput.txt", "w") as output:
            array = input.readline().split()
            k = input.readline()
            if len(array) < int(k):
                output.write("Inalid request given")
                return

            count = 0
            for i in range(len(array)):
                min = i

                for j in range(i+1, len(array)):
                    if int(array[min]) > int(array[j]):
                        min = j

                array[i], array[min] = array[min], array[i]
                count += 1

                if count == int(k):
                    output.write(array[int(k) - 1])
                    return

main()