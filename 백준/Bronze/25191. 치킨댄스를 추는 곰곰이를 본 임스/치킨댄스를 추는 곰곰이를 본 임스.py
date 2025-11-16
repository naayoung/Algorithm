import sys
input = sys.stdin.readline

N = int(input().strip())
A, B = map(int, input().split())

ans = A//2+B
if ans > N:
    print(N)
else:
    print(ans)