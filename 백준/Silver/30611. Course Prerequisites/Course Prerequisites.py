import sys
input = sys.stdin.readline

m = int(input().strip())
setA = set(input().split())
n = int(input().strip())
setB = input().split()

ans = 1
for b in setB:
    if b not in setA:
        ans = 0
        break
print(ans)