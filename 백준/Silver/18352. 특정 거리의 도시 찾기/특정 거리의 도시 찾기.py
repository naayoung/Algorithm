from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    q.append(x)
    visited[x] = 1
    cal[x] = 0

    while q:
        a = q.popleft()
        for b in graph[a]:
            if visited[b] == 0:
                q.append(b)
                visited[b] = 1

            if cal[b] == -1:
                cal[b] = cal[a]+1

                if cal[b] == k:
                    ans.append(b)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

ans = []
q = deque()
visited = [0]*(n+1)
cal = [-1]*(n+1)
bfs(x)

if len(ans) == 0:
    print(-1)
else:
    for a in sorted(ans):
        print(a)