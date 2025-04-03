N = int(input())

k = 1
time = 0

while N > 0:
    if N < k:
        k = 1
    N -= k
    k += 1
    time += 1

print(time)