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
                q.append(nx)

visited[r] = 1
q.append(r)
bfs()

for i in range(1, n+1):
    print(visited[i])