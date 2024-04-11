import sys
input = sys.stdin.readline

n, d = map(int, input().split())

count = 0
for i in range(1, n+1):
    for j in str(i):
        if int(j) == d:
            count += 1
print(count)