import sys
input = sys.stdin.readline

N, M, A, B = map(int, input().split())
dis = []
for _ in range(M):
    L, R = map(int, input().split())
    dis.append((L, R))

INF = int(1e9)
dp = [INF] * (N + 1)
dp[0] = 0

def room(num):
    for L, R in dis:
        if L <= num <= R:
            return True
    return False

for i in range(1, N+1):
    if room(i):
        continue
    if i-A >= 0 and not room(i-A):
        dp[i] = min(dp[i], dp[i-A]+1)
    if i-B >= 0 and not room(i-B):
        dp[i] = min(dp[i], dp[i-B] + 1)

if dp[N] != INF:
    print(dp[N])
else:
    print(-1)