import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

temp = [0 for _ in range(n+1)]
for i in range(n):
    temp[i+1] = max(temp[i] + num[i], num[i])
print(max(temp[1:]))