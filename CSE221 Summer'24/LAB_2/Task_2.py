def main():
    with open("input2.txt", "r") as input:
        len1 = int(input.readline())
        array1 = input.readline().split()
        len2 = int(input.readline())
        array2 = input.readline().split()
        new_array = []
 
        with open("output2.txt", "w") as output:
            i = 0
            j = 0

            while i < len1 and j < len2:
                if int(array1[i]) < int(array2[j]):
                    new_array.append((array1[i]))
                    i += 1
                
                else:
                    new_array.append(array2[j])
                    j += 1
            
            if i != len1:
                new_array = new_array + array1[i:]
            
            
            if j != len2:
                new_array = new_array + array2[j:]
            

            for num in new_array:
                output.write(f'{num} ')

main()