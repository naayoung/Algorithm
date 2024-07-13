import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n = int(input().strip())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (n+1)

def dfs(n):
    for i in graph[n]:
        if not visited[i]:
            visited[i] = n
            dfs(i)
dfs(1)

for i in range(2, n+1):
    print(visited[i])
