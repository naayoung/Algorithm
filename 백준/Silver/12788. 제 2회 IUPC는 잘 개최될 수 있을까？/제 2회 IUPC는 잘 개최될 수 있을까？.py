import sys
input = sys.stdin.readline

N = int(input().strip())
M, K = map(int, input().split())
A = list(map(int, input().split()))

mem = M*K
A.sort(reverse=True)

ans = 0
for n in range(1, N+1):
    a = sum(A[:n])
    if mem <= a:
        ans = n
        break
if ans == 0:
    print("STRESS")
else:
    print(ans)