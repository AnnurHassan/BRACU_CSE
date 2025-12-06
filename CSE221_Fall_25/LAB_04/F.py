import sys


n = int(sys.stdin.readline().strip())
x, y = list(map(int, sys.stdin.readline().strip().split()))

moves = []

if x - 1 >= 1 and y - 1 >= 1:
    moves.append((x-1, y-1))

if x > 1:
    moves.append((x-1, y))

if x - 1 >= 1 and y + 1 <= n:
    moves.append((x-1, y+1))

if y > 1:
    moves.append((x, y-1))

if y + 1 <= n:
    moves.append((x, y+1))

if x + 1 <= n and y - 1 >= 1:
    moves.append((x+1, y-1))

if x + 1 <= n:
    moves.append((x+1, y))

if x + 1 <= n and y + 1 <= n:
    moves.append((x+1, y+1))


# for i in range(len(moves)):
#     for j in range(len(moves)-1):
#         if moves[j][0] > moves[j+1][0]:
#             moves[j], moves[j+1] = moves[j+1], moves[j]
        
#         elif moves[j][0] == moves[j+1][0] and moves[j][1] > moves[j+1][1]:
#             moves[j], moves[j+1] = moves[j+1], moves[j]
moves.sort()

print(len(moves))
for i, j in moves:
    print(f"{i} {j}")