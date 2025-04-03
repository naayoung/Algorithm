import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input().strip())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, k, visited):
    return in_range(x, y) and visited[x][y] == 0 and graph[x][y] > k

def dfs(start_x, start_y, k, visited):
    stack = [(start_x, start_y)]
    visited[start_x][start_y] = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while stack:
        x, y = stack.pop()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, k, visited):
                visited[nx][ny] = 1
                stack.append((nx, ny))

def count_safe_areas(k):
    visited = [[0] * n for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(n):
            if can_go(i, j, k, visited):
                dfs(i, j, k, visited)
                count += 1
    
    return count

max_count = 0
for k in range(101):
    max_count = max(max_count, count_safe_areas(k))

print(max_count)