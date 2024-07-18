import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
max_distance = 100001
visited = [-1] * max_distance
q = deque()

def in_range(x):
    return 0 <= x < max_distance

def can_go(x):
    return in_range(x) and visited[x] == -1

def bfs():
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for nx in (x-1, x+1, x*2):
            if can_go(nx):
                if nx == x * 2:
                    visited[nx] = visited[x]
                    q.appendleft(nx) # 순간이동은 큐의 앞에 추가
                else:
                    visited[nx] = visited[x] + 1
                    q.append(nx)
q.append(n)
visited[n] = 0
bfs()