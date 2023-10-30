import sys, math
input = sys.stdin.readline

t = int(input())
num = [1, 2, 3]
answer = 0

def dp(n):
    if n == 1:
        answer = 1
    elif n == 2:
        answer = 2
    elif n == 3:
        answer = 4
    else:
        answer = dp(n-1)+dp(n-2)+dp(n-3)
    return answer

for i in range(t):
    n = int(input().strip())
    print(dp(n))