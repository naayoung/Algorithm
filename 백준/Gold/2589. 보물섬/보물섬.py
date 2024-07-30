from collections import deque
import sys
input = sys.stdin.readline

l, w = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(l)]
visited = [[-1]*w for _ in range(l)]
q = deque()

def in_range(x, y):
    return 0 <= x and x < l and 0 <= y and y < w

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] != -1 or graph[x][y] == 'W':
        return False
    return True

def bfs():
    global max_distance

    while q:
        x, y = q.popleft()
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = visited[x][y] + 1
                max_distance = max(max_distance, visited[nx][ny])
                q.append((nx, ny))

max_distance = 0
for i in range(l):
    for j in range(w):
        if graph[i][j] == 'L':
            visited = [[-1]*w for _ in range(l)]
            q = deque()
            
            q.append((i, j))
            visited[i][j] = 0
            bfs()

print(max_distance)