import sys
input = sys.stdin.readline

N, K = map(int, input().split())
countries = []

for _ in range(N):
    data = list(map(int, input().split()))
    countries.append(data)

countries.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1
for i in range(N):
    if i > 0:
        if countries[i][1:] == countries[i-1][1:]:
            pass
        else:
            rank = i+1

    if countries[i][0] == K:
        print(rank)
        break