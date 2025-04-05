import sys
input = sys.stdin.readline

H = int(input().strip())
W = int(input().strip())

ans = min(H, W)*100//2

print(ans)