def main():
    with open("input1a.txt", "r") as input_file:
        input_file.readline()

        with open("ouput1a.txt", "w") as ouput_file:
            for i in input_file:
                ouput_file.write(check(int(i)))


def check(num):
    if num % 2 == 0:
        return f"{num} is an Even number.\n"
    
    else:
        return f"{num} is a Odd number.\n"
    

main()



