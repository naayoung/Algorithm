import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0] * m for _ in range(n)]
q = deque()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or graph[x][y] == -1:
        return False
    return True

def bfs():
    while q:
        x, y = q.popleft()

        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = 1
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            visited[i][j] = 1
            q.append((i, j))

bfs()

answer = 0
for row in graph:
    for tomato in row:
        if tomato == 0:
            print(-1)
            exit(0)
        answer = max(answer, tomato)

print(answer - 1)