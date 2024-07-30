from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[-1]*m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(start_x, start_y):
    q = deque([(start_x, start_y)])
    visited[start_x][start_y] = 0
    
    while q:
        x, y = q.popleft()
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and visited[nx][ny] == -1 and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

# 목표 지점을 찾아 BFS를 시작
start_found = False
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:  # 시작점이 2로 표시된 경우
            start_x, start_y = i, j
            start_found = True
            break
    if start_found:
        break

# 시작점을 찾았다면 BFS를 실행
if start_found:
    bfs(start_x, start_y)

# 출력
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            # 0인 경우, 즉 바다인 경우에는 -1로 표시
            print(0, end=' ')
        else:
            # 방문할 수 없는 경우를 위해 -1 유지
            print(visited[i][j], end=' ')
    print()