import sys
input = sys.stdin.readline

A, B = map(int, input().split())
N = int(input().strip())
num = []
for _ in range(N):
    n = int(input().strip())
    num.append(n)
num.sort()

ans = abs(B-A)
for n in num:
    cnt = abs(B-n)+1
    ans = min(ans, cnt)

print(ans)