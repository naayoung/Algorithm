import sys
input = sys.stdin.readline

n = int(input().strip())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n+1)

def dfs(n):
    stack = [n]
    while stack:
        node = stack.pop()
        for i in graph[node]:
            if parent[i] == 0:
                parent[i] = node
                stack.append(i)

parent[1] = 1  # Root node (1) has no parent, set it to self or any value != 0
dfs(1)

for i in range(2, n+1):
    print(parent[i])
