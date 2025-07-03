import sys
input = sys.stdin.readline

a = int(input().strip())
m, n = map(int, input().split())
ans1, ans2 = 200, 200

if a == 1:
    if m > n:
        ans1 = min(m, n*2)
    else:
        ans2 = min(m*2, n)
else:
    ans1 = min(m/a*2, n)
    ans2 = min(m, n/a*2)


print(min(ans1, ans2))