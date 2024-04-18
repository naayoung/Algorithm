import sys
input = sys.stdin.readline

n = int(input()) #노드
m = int(input()) #간선

graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
count = -1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v):
    visited[v] = True

    global count
    count += 1
    
    for i in range(1, n+1):
        if not visited[i] and graph[v][i]:
            dfs(i)

dfs(1)
print(count)