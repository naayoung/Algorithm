import sys
input = sys.stdin.readline

n = int(input())
A = set(map(int, input().split()))

for i in range(1, n+2):
    if i not in A:
        print(i)
        break