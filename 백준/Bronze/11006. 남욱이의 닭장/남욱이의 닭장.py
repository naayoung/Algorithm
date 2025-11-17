import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N, M = map(int, input().split())
    print(M-(N-M), N-M)