import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
max_distance = 100001
visited = [0] * max_distance
q = deque()

min_path = 0
count = 0

def in_range(x):
    return 0 <= x < max_distance

def can_go(nx, x):
    return in_range(nx) and (visited[nx] == 0 or visited[nx] == visited[x] + 1)

def bfs():
    global count, min_path

    while q:
        x = q.popleft()
        if x == k:
            min_path = visited[x]
            count += 1
            continue
        for nx in (x - 1, x + 1, 2 * x):
            if can_go(nx, x):
                visited[nx] = visited[x] + 1
                q.append(nx)

visited[n] = 0
q.append(n)
bfs()

print(min_path)
print(count)

