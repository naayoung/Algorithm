import sys
input = sys.stdin.readline

a, b = map(int, input().split())
m = int(input().strip())

if b+m >= 60:
    a += (b+m)//60
    b = (b+m)%60
else:
    b = b+m
if a > 23:
    a = a - 24
print(a, b)