import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = list(map(int, input().split()))

prefix = [0 for _ in range(n+1)]
for i in range(n):
    prefix[i+1] = prefix[i] + num[i]

answer = -float('inf')
for i in range(k, n+1):
    answer = max(answer, prefix[i]-prefix[i-k])
print(answer)