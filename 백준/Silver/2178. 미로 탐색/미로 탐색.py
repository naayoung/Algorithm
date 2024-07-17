import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))
visited = [[0] * m for _ in range(n)]
q = deque()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or graph[x][y] == 0:
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

q.append((0, 0))
visited[0][0] = 1
bfs()
print(graph[n-1][m-1])