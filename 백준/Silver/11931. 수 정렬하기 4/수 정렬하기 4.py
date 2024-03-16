import sys

input = sys.stdin.readline

n = int(input())
num = []

for i in range(n):
    temp = int(input().strip())
    num.append(temp)
num.sort(reverse=True)

for i in num:
    print(i)