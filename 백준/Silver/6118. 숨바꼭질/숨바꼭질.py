from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    visited[x] = 1
    distance[x] = 0
    q.append(x)

    while q:
        a = q.popleft()
        for b in graph[a]:
            if visited[b] == 0:
                visited[b] = 1
                q.append(b)
            
            if distance[b] == -1:
                distance[b] = distance[a]+1

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
visited = [0]*(n+1)
distance = [-1]*(n+1)
bfs(1)

max_distance = max(distance)
h = distance.index(max_distance)
cnt = distance.count(max_distance)
print(h, max_distance, cnt)