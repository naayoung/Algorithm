import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
max_range = 10**5 + 1
visited = [0] * max_range
q = deque()

def in_range(x):
    return 0 <= x and x < max_range

def can_go(x):
    return in_range(x) and visited[x] == 0
    
def bfs():
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x] - 1)
            return
        for nx in (x - 1, x + 1, x * 2):
            if can_go(nx):
                visited[nx] = visited[x] + 1
                q.append(nx)
q.append(n)
visited[n] = 1
bfs()