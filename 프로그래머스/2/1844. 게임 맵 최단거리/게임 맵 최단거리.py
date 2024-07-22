from collections import deque

def solution(maps):
    rows, cols = len(maps), len(maps[0])
    visited = [[-1] * cols for _ in range(rows)]
    
    def in_range(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def can_go(x, y):
        if not in_range(x, y):
            return False
        if visited[x][y] != -1 or maps[x][y] == 0:
            return False
        return True
    
    def bfs():
        visited[0][0] = 1
        q = deque([(0, 0)])
        while q:
            x, y = q.popleft()
            if x == rows - 1 and y == cols - 1:  # 목적지에 도달하면 즉시 종료
                return visited[x][y]
                
            dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if can_go(nx, ny):
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
        return -1
    
    return bfs()