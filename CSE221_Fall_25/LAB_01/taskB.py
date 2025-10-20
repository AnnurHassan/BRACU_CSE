t = int(input())
for i in range(t):
    test_case = input().strip().split(" ")
    
    if test_case[2] == '+':
        result = int(test_case[1]) + int(test_case[3])
        print(result)
    
    elif test_case[2] == '-':
        result = int(test_case[1]) - int(test_case[3])
        print(result)

    elif test_case[2] == '*':
        result = int(test_case[1]) * int(test_case[3])
        print(result)

    elif test_case[2] == '/':
        result = int(test_case[1]) / int(test_case[3])
        print(result)