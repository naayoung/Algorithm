import sys
input = sys.stdin.readline

N = int(input())
temp = []

for i in range(N):
    temp.append(int(input()))
temp.sort()

for i in temp:
    print(i)