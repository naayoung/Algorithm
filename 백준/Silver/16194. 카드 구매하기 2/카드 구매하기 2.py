import sys
input = sys.stdin.readline

N = int(input().strip())
P = [0]+list(map(int, input().split()))

INF = 10**9
dp = [INF]*(N+1)
dp[0] = 0

for n in range(1, N+1):
    for p in range(1, n+1):
        dp[n] = min(dp[n], dp[n-p]+P[p])
print(dp[N])