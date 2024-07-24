import sys
input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    s = int(input().strip())
    for i in range(2, 1000001):
        if s % i == 0:
            print("NO")
            break
        if i == 1000000:
            print("YES")