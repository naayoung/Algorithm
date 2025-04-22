import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

visited = [False]*(N+1)
dist = [0]*(N+1)

def dfs(n):
    visited[n] = True
    for neighbor, w in graph[n]:
        if not visited[neighbor]:
            dist[neighbor] = dist[n]+w
            dfs(neighbor)

dfs(1)
print(max(dist))