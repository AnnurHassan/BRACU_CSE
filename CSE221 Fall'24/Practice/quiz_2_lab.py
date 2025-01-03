arr_1 = [1, 3, 5, 8, 7, 9, 15, 18, 25]
arr_2 = [1, 3, 8, 9, 20, 30, 45, 150, 200]

max_val = 0
max_idx = len(arr_1) - 1
while max_idx >= 0:
    if arr_1[max_idx] in arr_2:
        max_val = arr_1[max_idx]
        break

    max_idx -= 1

print(max_val)