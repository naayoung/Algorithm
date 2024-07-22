import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
friend = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = tuple(map(int, input().split()))
    friend[a][b] = 1
    friend[b][a] = 1
visited = [0] * (n+1) #뎁스
q = deque()

def bfs():
    while q:
        x = q.popleft()
        for nx in range(1, n+1):
            if visited[nx] == 0 and friend[x][nx] == 1: #연결된 노드인지 확인
                visited[nx] = visited[x] + 1
                q.append(nx)
visited[1] = 1
q.append(1)
bfs()

result = 0
for i in range(2,n+1):
    # 본인이거나 친구거나, 친구의 친구거나 경우의 수가 최대 3개
    if visited[i] < 4 and visited[i] != 0:
        result += 1
print(result)