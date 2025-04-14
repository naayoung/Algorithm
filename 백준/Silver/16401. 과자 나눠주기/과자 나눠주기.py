import sys
input = sys.stdin.readline

M, N = map(int, input().split())
snack = list(map(int, input().split()))

def count(m):
    cnt = 0
    for s in snack:
        cnt += s//m
    return cnt

l, r = 1, max(snack)
ans = 0

while l <= r:
    m = (l+r)//2
    
    if count(m) >= M:
        ans = m
        l = m+1
    else:
        r = m-1
print(ans)