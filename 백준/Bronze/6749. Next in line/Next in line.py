import sys
input = sys.stdin.readline

Y = int(input().strip())
M = int(input().strip())

ans = M + (M-Y)
print(ans)