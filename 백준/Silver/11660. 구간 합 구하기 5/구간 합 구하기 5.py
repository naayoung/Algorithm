import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

#누적합
prefix = [[0 for _ in range(n+1)] for _ in range(n+1)]
for y in range(n):
    for x in range(n):
        prefix[y+1][x+1] = prefix[y][x+1] + prefix[y+1][x] - prefix[y][x] + graph[y][x]

answer = []
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    tmp = prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1]
    answer.append(tmp)

for ans in answer:
    print(ans)