import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

d = abs(a) + abs(b)

if d <= c and (c-d)%2 == 0:
    print("YES")
else:
    print("NO")