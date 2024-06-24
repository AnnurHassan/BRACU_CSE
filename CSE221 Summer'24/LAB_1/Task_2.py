def main():
    with open("input2.txt", "r") as input:
        input.readline()

        with open("output2.txt", "w") as output:
            array = input.readline().split(" ")
            bubbleSort(array)
            output.write

            
def bubbleSort(arr):
    for i in range(len(arr) - 1):

        for j in range(len(arr) - i - 1):
            if (arr[j]) > (arr[j + 1]):
                arr[j], arr[j + 1] = (arr[j + 1]), (arr[j])
    

main()
#unfinished