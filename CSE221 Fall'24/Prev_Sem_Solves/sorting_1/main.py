with open("input.txt", "r") as input:
    with open("output.txt", "w") as output:
        n = int(input.readline())
        arr = [int(i) for i in input.readline().strip().split(" ")]
        count = 0

        for i in range(n):
            min = i

            for j in range(i,n):
                
                if arr[min] > arr[j]:
                    min = j
            
            if min != i:
                arr[i], arr[min] = arr[min], arr[i]
                count += 1
        
        output.write(f"{count}")