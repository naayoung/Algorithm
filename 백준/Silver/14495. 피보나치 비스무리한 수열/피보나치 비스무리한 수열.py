import sys

input = sys.stdin.readline

N = int(input().rstrip())

f = [1]*(N+1)

for i in range(3, N+1):

    f[i] = f[i-1] + f[i-3]

print(f[N-1])