import sys
input = sys.stdin.readline

# 입력받기
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 깊이 배열 초기화
depth = [-1] * (n + 1)

# 각 노드의 인접 노드를 오름차순으로 정렬
for i in range(1, n + 1):
    graph[i].sort()

def dfs(start):
    stack = [(start, 0)]  # 스택에 (노드, 깊이) 형태로 저장
    while stack:
        x, d = stack.pop()
        if depth[x] == -1:  # 방문하지 않은 경우
            depth[x] = d
            for nx in reversed(graph[x]):  # 오름차순 방문을 위해 역순으로 넣기
                if depth[nx] == -1:
                    stack.append((nx, d + 1))

# DFS 시작
dfs(r)

# 결과 출력
for i in range(1, n + 1):
    print(depth[i])