import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x and x < h and 0 <= y and y < w

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or graph[x][y] == 0:
        return False
    return True

def dfs(x, y):
    dxs = [0, 1, 0, -1, 1, 1, -1, -1]
    dys = [1, 0, -1, 0, 1, -1, 1, -1]
    visited[x][y] = 1

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny):
            dfs(nx, ny)

while True:
    w, h = tuple(map(int, input().split()))

    if w == 0 and h == 0:
        break
    else:
        graph = []
        for _ in range(h):
            graph.append(list(map(int, input().split())))

        visited = [[0] * w for _ in range(h)]
        land = 0

        for i in range(h):
            for j in range(w):
                if can_go(i, j):
                    visited[i][j] = 1
                    land += 1

                    dfs(i, j)
        print(land)