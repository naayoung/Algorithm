import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
	a, b = map(int, input().split())
	graph[b].append(a)

def bfs(i):
	q = deque([i])
	visited = [0] * (n + 1)
	visited[i] = 1
	cnt = 1
	while q:
		i = q.popleft()
		for j in graph[i]:
			if not visited[j]:
				q.append(j)
				visited[j] = 1
				cnt += 1
	return cnt

max_cnt = 1
answer = []
for i in range(1, n + 1):
	cnt = bfs(i)
	if cnt > max_cnt: # 최장 길이 갱신
		max_cnt = cnt
		answer = [] # answer 배열 초기화
		answer.append(i)
	elif cnt == max_cnt:
		answer.append(i)

print(*answer)