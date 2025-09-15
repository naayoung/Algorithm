import sys
input = sys.stdin.readline

j = input().strip()
d = input().strip()

if len(j) >= len(d):
    print("go")
else:
    print("no")