import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def in_range(x, y, n, m):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y, graph, visited, n, m):
    if not in_range(x, y, n, m):
        return False
    if visited[x][y] == 1 or graph[x][y] == 0:
        return False
    return True

def dfs(x, y, graph, visited, n, m):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y, graph, visited, n, m):
            visited[new_x][new_y] = 1
            dfs(new_x, new_y, graph, visited, n, m)

t = int(input().strip())
for _ in range(t):
    m, n, k = tuple(map(int, input().split()))

    graph = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = tuple(map(int, input().split()))
        graph[y][x] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if can_go(i, j, graph, visited, n, m):
                visited[i][j] = 1
                count += 1

                dfs(i, j, graph, visited, n, m)
    print(count)