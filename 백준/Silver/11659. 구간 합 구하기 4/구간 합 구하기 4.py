import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
nums = [0]
s = 0

for i in range(n):
    s += num[i]
    nums.append(s)

for x in range(m):
    i, j = map(int, input().split())
    answer = nums[j] - nums[i-1]
    print(answer)