import sys
sys.setrecursionlimit(10000)  # 재귀 제한 해제
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
count = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

def dfs(v):
    visited[v] = True

    for i in range(1, N+1):
        if not visited[i] and graph[v][i]:
            dfs(i)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)