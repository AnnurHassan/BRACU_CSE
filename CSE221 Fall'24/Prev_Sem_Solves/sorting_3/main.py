with open("input.txt", "r") as input:
    with open("output.txt", "w") as output:
        n = int(input.readline())
        arr = [int(i) for i in input.readline().strip().split(" ")]
        brr = []    
        left = 0
        right = n - 1
        last_added = 0

        while left <= right:
            
