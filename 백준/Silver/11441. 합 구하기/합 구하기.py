import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
m = int(input())
#누적합
prefix = [0 for _ in range(n+1)]
for i in range(n):
    prefix[i+1] = prefix[i] + num[i]

answer = []
for i in range(m):
    i, j = map(int, input().split())
    answer.append(prefix[j]-prefix[i-1])

for ans in answer:
    print(ans)