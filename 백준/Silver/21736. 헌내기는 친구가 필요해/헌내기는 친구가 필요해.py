import sys
#sys.setrecursionlimit(10**6)
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input().strip()))
visited = [[0] * m for _ in range(n)]
count = 0
q = deque()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or graph[x][y] == 'X':
        return False
    return True

def dfs(x, y):
    global count
    visited[x][y] = 1

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            if graph[nx][ny] == 'P':
                count += 1

            visited[nx][ny] = 1
            dfs(nx, ny)

def bfs():
    global count

    while q:
        x, y = q.popleft()
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                if graph[nx][ny] == 'P':
                    count += 1

                visited[nx][ny] = 1
                q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            x, y = i, j
            break

#dfs(x, y)
q.append((x, y))
visited[x][y] = 1
bfs()

if count > 0:
    print(count)
else:
    print('TT')