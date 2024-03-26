import sys
input = sys.stdin.readline

n, k = map(int, input().split())
count = 0
girl, boy = [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]

for i in range(n):
    s, y = map(int, input().split())

    if s == 0:
        girl[y-1] += 1
    else:
        boy[y-1] += 1

for i in girl:
    if i%k == 0:
        count += i//k
    else:
        count += i//k + 1

for i in boy:
    if i%k == 0:
        count += i//k
    else:
        count += i//k + 1

print(count)