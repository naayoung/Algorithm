import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, k):
    return in_range(x, y) and not visited[x][y] and graph[x][y] > k

def dfs(x, y, k):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    stack = [(x, y)]
    visited[x][y] = 1

    while stack:
        x, y = stack.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, k):
                visited[nx][ny] = 1
                stack.append((nx, ny))

def safe_area(k):
    global visited
    visited = [[0] * n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if can_go(i, j, k):
                dfs(i, j, k)
                count += 1
    return count

max_count = 0
max_height = max(map(max, graph))
for k in range(max_height):
    max_count = max(max_count, safe_area(k))

print(max_count)