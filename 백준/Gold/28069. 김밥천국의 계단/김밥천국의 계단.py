import sys
input = sys.stdin.readline

N, K = map(int, input().split())
INF = int(1e9)
MAX = N+N//2+1
dp = [INF]*MAX
dp[0] = 0

for i in range(0, N+1):
    if dp[i] == INF:
        continue
    if i+1 < MAX:
        dp[i+1] = min(dp[i+1], dp[i]+1)
    if i+i//2 < MAX:
        dp[i+i//2] = min(dp[i+i//2], dp[i]+1)

if dp[N] <= K:
    print("minigimbob")
else:
    print("water")