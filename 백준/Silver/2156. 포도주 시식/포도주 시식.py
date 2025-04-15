import sys
input = sys.stdin.readline

n = int(input())
gra = [int(input()) for _ in range(n)]

if n == 1:
    print(gra[0])
elif n == 2:
    print(gra[0] + gra[1])
else:
    dp = [0]*n
    dp[0] = gra[0]
    dp[1] = gra[0] + gra[1]
    dp[2] = max(gra[0] + gra[2], gra[1] + gra[2], dp[1])

    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2] + gra[i], dp[i-3] + gra[i-1] + gra[i])

    print(dp[n-1])