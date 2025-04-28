import sys
input = sys.stdin.readline

N = int(input().strip())
num = [int(input().strip()) for _ in range(N)]

num.sort()
max_sum = -1

for i in range(N - 1, 1, -1):
    if num[i-2] + num[i-1] > num[i]:
        max_sum = num[i-2] + num[i-1] + num[i]
        break 

print(max_sum)