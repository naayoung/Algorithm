from collections import deque
import sys
input = sys.stdin.readline

tc = int(input().strip())
for _ in range(tc):
    l = int(input().strip())
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    visited = [[0]*l for _ in range(l)]
    step = [[0]*l for _ in range(l)]
    count = 0
    q = deque()

    def in_range(x, y):
        return 0 <= x and x < l and 0 <= y and y < l

    def can_go(x, y):
        if not in_range(x, y):
            return False
        if visited[x][y] == 1:
            return False
        return True

    def bfs():
        global count
        while q:
            x, y = q.popleft()

            dxs = [-2, -2, -1, -1,  1, 1,  2, 2]
            dys = [-1,  1, -2,  2, -2, 2, -1, 1]
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if can_go(nx, ny):
                    visited[nx][ny] = 1
                    step[nx][ny] = step[x][y] + 1
                    q.append((nx, ny))
            if visited[r2][c2]:
                count = step[r2][c2]
                return
    visited[r1][c1] = 1
    step[r1][c1] = 0
    q.append((r1, c1))
    bfs()
    print(count)