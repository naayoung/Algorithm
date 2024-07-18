import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
max_distance = 100001
visited = [-1] * max_distance	# 이전 경로를 저장하는 배열
q = deque()

answer = []

def in_range(x):
    return 0 <= x < max_distance

def bfs():
    while q:
        x = q.popleft()
        if x == k:
            while x != n:     	# 인덱스 값이 N인 경우, 도착한 것이니 종료
                answer.append(x)	# 경로에 추가
                x = visited[x]		# 현재 위치를 이전 위치로 갱신
            answer.append(n)
            break
        for nx in (x-1, x+1, x*2):
            if in_range(nx) and visited[nx] == -1:
                visited[nx] = x
                q.append(nx)

visited[n] = n
q.append(n)
bfs()

print(len(answer)-1)
print(*answer[::-1])