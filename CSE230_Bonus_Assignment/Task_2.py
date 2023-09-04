import random 

t = int(input())
m = 0
for i in range(t):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    distance = (pow(x,2) + pow(y,2)) ** 0.5
    if distance <= 1:
        m += 1

pi = m * 4 / t
print(pi)