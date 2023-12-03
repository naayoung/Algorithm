import sys
input = sys.stdin.readline

n = int(input().strip())
box = ["@@@@@", "@", "@@@@@", "@", "@"]

for i in box:
    for j in range(n):
        print(i*n)