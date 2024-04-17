import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[False]*(N+1) for _ in range(N+1)]

for _ in range(M):
    X, Y = map(int, input().split())
    graph[X][Y] = True
    graph[Y][X] = True

visited1 = [False] * (N+1) # dfs 방문
visited2 = [False] * (N+1) # bfs 방문

def dfs(v):
    visited1[v] = True
    print(v, end=' ')

    for i in range(1, N+1):
        if graph[v][i] and not visited1[i]:
            dfs(i)

def bfs(v):
    q = deque([v])
    visited2[v] = True

    while q:
        v = q.popleft()
        print(v, end=' ')

        for i in range(1, N+1):
            if graph[v][i] and not visited2[i]:
                q.append(i)
                visited2[i] = True

dfs(V)
print()
bfs(V)