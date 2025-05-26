import sys
input = sys.stdin.readline

z = int(input().strip())
for _ in range(z):
    n, k = map(int, input().split())
    tc = list(map(int, input().split()))
    tc.sort(reverse=True)

    print(max(sum(tc[k:]), tc[0]))