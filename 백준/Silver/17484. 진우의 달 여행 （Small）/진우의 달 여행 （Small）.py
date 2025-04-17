import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1]
answer = int(1e9)

def dfs(i, j, pr, total):
    global answer
    
    if i == N:
        answer = min(answer, total)
        return
    for d in range(3):
        if d != pr:
            nj = j + dx[d]
            if 0 <= nj < M:
                dfs(i+1, nj, d, total+space[i][nj])

for j in range(M):
    dfs(1, j, -1, space[0][j])
print(answer)