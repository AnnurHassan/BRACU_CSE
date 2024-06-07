def main():
    with open("input1b.txt", "r") as input_file:
        input_file.readline()
        
        with open("output1b.txt", "w") as output_file:
            for i in input_file:
                array = i.split()
                result = f"The result of {array[1]} {array[2]} {array[3]} is {calculate(array)}\n"
                output_file.write(result)

                


def calculate(array):
    if array[2] == "+":
        return (int(array[1]) + int(array[3]))
    
    elif array[2] == "-":
        return (int(array[1]) - int(array[3]))
    
    elif array[2] == "*":
        return (int(array[1]) * int(array[3]))
    
    elif array[2] == "/":
        return (int(array[1]) / int(array[3]))
    

main()