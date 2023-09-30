import sys
input = sys.stdin.readline

n = int(input())
nums = []

for i in range(n):
    number = list(map(str, input().split()))
    nums.append(number)

nums.sort(key = lambda x: (int(x[0]),int(x[1])))

for i in nums:
    print(' '.join(i))