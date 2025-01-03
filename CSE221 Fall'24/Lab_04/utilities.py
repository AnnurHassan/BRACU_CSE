def print_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print(mat[i][j], end = " ")
        
        print()

def print_dict(dict):
    for key, value in dict.items():
        print(f'{key} : {", ".join(map(str, value))}')

def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")
    
    print()