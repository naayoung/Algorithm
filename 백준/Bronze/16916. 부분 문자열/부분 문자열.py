import sys
input = sys.stdin.readline

s = str(input().strip())
p = str(input().strip())

if p in s:
    print(1)
else:
    print(0)