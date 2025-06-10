from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
picture = []
for _ in range(n):
    picture.append(list(map(int, input().split())))
visited = [[0]*m for _ in range(n)]

def in_range(row, col):
    return 0 <= row < n and 0 <= col < m

def can_go(row, col):
    if not in_range(row, col):
        return False
    if visited[row][col] == 1 or picture[row][col] == 0:
        return False
    return True

def bfs(row, col):
    drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]
    q = deque()
    q.append((row, col))
    visited[row][col] = 1

    size = 1

    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = r+dr, c+dc

            if can_go(nr, nc):
                visited[nr][nc] = 1
                q.append((nr, nc))
                size += 1
    return size


answer = []
for r in range(n):
    for c in range(m):
        if can_go(r, c):
            answer.append(bfs(r, c))


if answer:
    print(len(answer))
    print(max(answer))
else:
    print(0)
    print(0)