import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = list(map(int, input().split()))

prefix = [0 for _ in range(n+1)]
for i in range(n):
    prefix[i+1] = prefix[i] + num[i]

answer = []
for i in range(k, n+1):
    answer.append(prefix[i]-prefix[i-k])
print(max(answer))