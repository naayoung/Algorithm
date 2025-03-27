import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0]*2 for _ in range(N)]
ans = 0

#A시작
dp[0][0] = A[0]
#B시작
dp[0][1] = B[0]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][0], dp[i-1][1]+K) + A[i]
    dp[i][1] = min(dp[i-1][1], dp[i-1][0]+K) + B[i]

ans = min(dp[N-1][0], dp[N-1][1])
print(ans)