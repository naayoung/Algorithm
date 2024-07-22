import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * (n+1)
depth = [-1] * (n+1)
q = deque()
count = 1

for i in range(n+1):
    graph[i].sort()

def bfs():
    global count
    while q:
        x = q.popleft()

        for nx in graph[x]:
            if visited[nx] == 0:
                count += 1
                visited[nx] = count
                depth[nx] = depth[x] + 1
                q.append(nx)

visited[r] = 1
depth[r] = 0
q.append(r)
bfs()

answer = 0
for i in range(1, n+1):
    answer += depth[i] * visited[i]
print(answer)