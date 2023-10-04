import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sites = dict([list(map(str, input().split())) for _ in range(n)])
q = [str(input().strip()) for _ in range(m)]

for i in q:
    if i in sites:
        print(sites[i])
