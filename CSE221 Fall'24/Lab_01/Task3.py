def main():
    with open("input3.txt", "r") as input:
        with open("output3.txt", "w") as output:
            n = int(input.readline())
            ids = [int(i) for i in input.readline().strip().split(" ")]
            marks = [int(i) for i in input.readline().strip().split(" ")]
            data = {}

            for i in range(n):
                data[marks[i]] = ids[i]

            for i in range(n):
                max = i
                for j in range(i + 1, n):
                    if marks[max] < marks[j]:
                        max = j

                    if marks[max] == marks[j]:
                        if ids[max] > ids[j]:
                            max = j

                if max != i:
                    marks[i], marks[max] = marks[max], marks[i]
                
                output.write(f"ID: {ids[max]} Mark: {marks[i]}")
                print(f"ID: {ids[max]} Mark: {marks[i]}")
    

if __name__ == "__main__":
    main()
