from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

INF = 10**9
fire = [[INF]*c for _ in range(r)]  # 불 도착 최소시간
cnt = [[-1]*c for _ in range(r)]    # 지훈 도착시간
visitedF = [[0]*c for _ in range(r)]
visitedJ = [[0]*c for _ in range(r)]

drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(R, C):
    return 0 <= R < r and 0 <= C < c

def can_go(R, C, visited):
    return in_range(R, C) and graph[R][C] != '#' and visited[R][C] == 0

def bfs_fire():
    q = deque()

    for R in range(r):
        for C in range(c):
            if graph[R][C] == 'F':
                visitedF[R][C] = 1
                fire[R][C] = 0
                q.append((R, C))
    while q:
        R, C = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = R+dr, C+dc
            if can_go(nr, nc, visitedF):
                visitedF[nr][nc] = 1
                fire[nr][nc] = fire[R][C] + 1
                q.append((nr, nc))

def bfs_jihun():
    q = deque()

    sR = sC = -1
    for R in range(r):
        for C in range(c):
            if graph[R][C] == 'J':
                sR, sC = R, C
                break
        if sR != -1: break

    visitedJ[sR][sC] = 1
    cnt[sR][sC] = 0
    q.append((sR, sC))

    if sR == 0 or sR == r-1 or sC == 0 or sC == c-1:
        return 1

    while q:
        R, C = q.popleft()
        t = cnt[R][C]
        for dr, dc in zip(drs, dcs):
            nr, nc = R+dr, C+dc

            if not in_range(nr, nc):
                return t + 1

            # 이동 가능: 벽X, 미방문, (불이 안 오거나) 불 시간 > 지훈의 다음 시간
            if can_go(nr, nc, visitedJ) and fire[nr][nc] > t + 1:
                visitedJ[nr][nc] = 1
                cnt[nr][nc] = t + 1
                q.append((nr, nc))
    return -1

bfs_fire()
ans = bfs_jihun()

if ans == -1:
    print("IMPOSSIBLE")
else:
    print(ans)
