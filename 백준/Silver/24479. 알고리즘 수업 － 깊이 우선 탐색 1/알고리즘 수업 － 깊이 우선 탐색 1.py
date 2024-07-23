import sys
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
    graph[i].sort(reverse=True) #스택을 사용할 때는 역순으로 정렬하면 작은 번호부터 방문

def dfs(start):
    global count
    stack = [start]

    while stack:
        x = stack.pop()
        if visited[x] == 0:
            count += 1
            visited[x] = count
            for nx in graph[x]:
                if visited[nx] == 0:
                    stack.append(nx)

dfs(r)

for i in range(1, n+1):
    print(visited[i])