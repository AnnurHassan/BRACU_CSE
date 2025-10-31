import sys


n = int(sys.stdin.readline().strip())
arr = sys.stdin.readlines()

for i in range(n):
    for j in range(n-1):
        temp_arr1 = arr[j].strip().split()
        name1, time1 = temp_arr1[0], temp_arr1[6]
        temp_arr2 = arr[j+1].strip().split()
        name2, time2 = temp_arr2[0], temp_arr2[6]

        if name1 > name2:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        
        elif name1 == name2:
            h, m = time1.split(":")
            time1 = int(h) * 60 + int(m)
            
            h, m = time2.split(":")
            time2 = int(h) * 60 + int(m)

            if time1 < time2:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                

for i in arr:
    print(i.strip())