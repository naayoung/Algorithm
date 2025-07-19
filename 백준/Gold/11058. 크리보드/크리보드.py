import sys
input = sys.stdin.readline

n = int(input().strip())

dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = dp[i-1] + 1

    for j in range(3, i+1):
        dp[i] = max(dp[i], dp[i-j] * (j-1))

print(dp[n])
