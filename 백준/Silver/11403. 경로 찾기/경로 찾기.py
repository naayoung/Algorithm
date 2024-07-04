import sys
input = sys.stdin.readline

n = int(input().strip())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


for k in range(n): #경유
    for i in range(n): #출발
        for j in range(n): #도착
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for i in range(n):
    print(*graph[i])