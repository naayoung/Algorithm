import sys
input = sys.stdin.readline

n = int(input())
num = [int(input()) for i in range(n)]
num.sort()

for i in num:
    print(i)