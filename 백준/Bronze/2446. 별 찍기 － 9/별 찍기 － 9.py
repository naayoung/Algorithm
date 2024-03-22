import sys

input = sys.stdin.readline

N = int(input().strip())

for i in range(N, 0, -1):
    temp = 2*i-1
    print(" "*(N-i) + "*"*temp)
for j in range(2, N+1):
    temp = 2*j-1
    print(" "*(N-j) + "*"*temp)