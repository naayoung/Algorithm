import sys

input = sys.stdin.readline

n = int(input())
count = 0

for i in range(1, n+1):
    if i < 100:
        count += 1
    else:
        num = list(map(int, str(i))) #분리
        if num[0] - num[1] == num[1] - num[2]:
            count += 1
print(count)
