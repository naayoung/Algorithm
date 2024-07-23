import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
depth = [-1] * (n+1)

for i in range(n+1):
    graph[i].sort(reverse=True)

def dfs(x):
    for nx in graph[x]:
        if depth[nx] == -1:
            depth[nx] = depth[x] + 1
            dfs(nx)

depth[r] = 0
dfs(r)

for i in range(1, n+1):
    print(depth[i])