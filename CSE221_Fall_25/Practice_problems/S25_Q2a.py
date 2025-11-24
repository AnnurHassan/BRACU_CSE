hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
temp = [29, 28, 24, 20, 16, 12, 10, 9, 11, 15, 19, 23]


# Linear Search --> O(n) 
def Linear_Search_Lowest_temp(hour, temp):
    for i in range(1, len(hour) - 1):
        
        if temp[i - 1] >= temp[i] <= temp[i + 1]:
           return (f"Lower Temp -> {temp[i]} at {hour[i]}")
        

        


