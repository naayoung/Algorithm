from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))
visited = [[0]*m for _ in range(n)]
ans_count = [[0]*m for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m
def can_go(r, c):
    if not in_range(r, c):
        return False
    if visited[r][c] == 1 or graph[r][c] == 0:
        return False
    return True

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    ans_count[r][c] = 1

    drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = r+dr, c+dc

            if can_go(nr, nc):
                q.append((nr, nc))
                visited[nr][nc] = 1
                ans_count[nr][nc] = ans_count[r][c] + 1
                
for r in range(n):
    for c in range(m):
        if can_go(r, c):
            bfs(r, c)

print(ans_count[n-1][m-1])