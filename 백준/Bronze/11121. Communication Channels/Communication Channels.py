import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    a, b = input().split()
    if a == b:
        print("OK")
    else:
        print("ERROR")