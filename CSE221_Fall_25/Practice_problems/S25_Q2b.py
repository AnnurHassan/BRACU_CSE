hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
temp = [29, 28, 24, 20, 16, 12, 10, 9, 11, 15, 19, 23]


# Binary Search --> O(log n)
def Binary_Search_Lowest_temp(hour, temp):
    low = 0
    high = len(hour)

    while low <= high:
        mid = (low + high) // 2
        if temp[mid - 1] > temp[mid] > temp[mid + 1]:
            low = mid + 1
        
        elif temp[mid - 1] < temp[mid] < temp[mid + 1]:
            high = mid - 1
        
        else:
            return hour[mid], temp[mid]
        

hour, temp = Binary_Search_Lowest_temp(hour, temp)
print(f"Lower Temp -> {temp} at {hour}")