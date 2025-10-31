import sys


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    std_id = [int(i) for i in sys.stdin.readline().strip().split()]
    marks = [int(i) for i in sys.stdin.readline().strip().split()]
    count = 0
    if n > 1000:
        break

    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if marks[j] > marks[max_idx] or (marks[j] == marks[max_idx] and std_id[j] < std_id[max_idx]):
                max_idx = j

        if max_idx != i:
            marks[i], marks[max_idx] = marks[max_idx], marks[i]
            std_id[i], std_id[max_idx] = std_id[max_idx], std_id[i]
            count += 1

    print(f"Minimum swaps: {count}")
    for i in range(len(std_id)):
        print(f"ID: {std_id[i]} Mark: {marks[i]}")
