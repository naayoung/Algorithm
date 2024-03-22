import sys

input = sys.stdin.readline

N = int(input().strip())

for j in range(1, N):
    print("*"*j + " "*(2*(N-j))+"*"*j)
for i in range(N, 0, -1):
    print("*"*i + " "*(2*(N-i))+"*"*i)