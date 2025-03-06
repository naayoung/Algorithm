import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = items[i - 1]
    for k in range(K + 1):
        if k >= w:
            dp[i][k] = max(dp[i-1][k], dp[i-1][k-w] + v)
        else:
            dp[i][k] = dp[i-1][k]

print(dp[N][K])