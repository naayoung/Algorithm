import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or graph[x][y] == 0:
        return False
    return True

def dfs(x, y):
    global count
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                #dfs(nx, ny)
                count += 1
                visited[nx][ny] = 1

                stack.append((nx, ny))

answer = []
for i in range(n):
    for j in range(m):
        if can_go(i, j):
            count = 1
            visited[i][j] = 1

            dfs(i, j)
            answer.append(count)
if answer:
    print(len(answer))
    print(max(answer))
else:
    print(0)
    print(0)