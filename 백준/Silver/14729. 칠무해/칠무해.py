import sys

input = sys.stdin.readline

n = int(input())
num = []

for i in range(n):
    temp = float(input().strip())
    num.append(temp)

num.sort()

for i in range(7):
    print("{:.3f}".format(num[i]))