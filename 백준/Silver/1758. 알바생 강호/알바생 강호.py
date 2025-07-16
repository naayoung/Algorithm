import sys
input = sys.stdin.readline

n = int(input().strip())
tips = []
for _ in range(n):
    t = int(input().strip())
    tips.append(t)
tips.sort(reverse=True)

ans = 0
for p in range(n):
    tip = tips[p]-(p+1-1)
    if tip < 0:
        tip = 0
    ans += tip

print(ans)