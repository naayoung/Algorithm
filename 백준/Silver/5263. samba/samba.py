import sys
input = sys.stdin.readline
n, k = map(int, input().split())
ID = {}

for _ in range(n):
    tmp = int(input().strip())
    if tmp not in ID:
        ID[tmp] = 1
    else:
        ID[tmp] += 1

for key, values in ID.items():
    if values%k != 0:
        print(key)