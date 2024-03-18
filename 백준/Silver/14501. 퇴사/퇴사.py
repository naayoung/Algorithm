import sys

input = sys.stdin.readline

n = int(input())
s = []

for i in range(n):
    t, p = map(int, input().split())
    s.append((t, p))

dp = [0 for i in range(n+1)]

for i in range(n):
    for j in range(i+s[i][0], n+1):
        if dp[j] < dp[i]+s[i][1]:
            dp[j] = dp[i]+s[i][1]
print(dp[-1])