import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * (n+1)
count = 0

for i in range(n+1):
    graph[i].sort(reverse=True)

def dfs(x):
    global count
    count += 1
    visited[x] = count

    for nx in graph[x]:
        if visited[nx] == 0:
            dfs(nx)

dfs(r)

for i in range(1, n+1):
    print(visited[i])