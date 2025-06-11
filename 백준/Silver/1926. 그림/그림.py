from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0]*m for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

def can_go(r, c):
    if not in_range(r, c):
        return False
    if visited[r][c] == 1 or graph[r][c] == 0:
        return False
    return True

def bfs(r, c):
    drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]
    q = deque()
    q.append((r, c))
    visited[r][c] = 1

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
 


ans = []
for r in range(n):
    for c in range(m):
        if can_go(r, c):
            ans.append(bfs(r, c))

if len(ans) != 0:
    print(len(ans))
    print(max(ans))
else:
    print(0)
    print(0)