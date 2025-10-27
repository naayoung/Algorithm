import sys
input = sys.stdin.readline


T = int(input().strip())
case1, case2 = [], []
for _ in range(T):
    N = int(input().strip())
    case1 = set(map(int, input().split()))

    M = int(input().strip())
    case2 = list(map(int, input().split()))

    for c in case2:
        if c in case1:
            print(1)
        else:
            print(0)