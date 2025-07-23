from collections import deque

N = int(input())
countries = []
edges_info = []
for _ in range(N):
    line = input().strip()
    countries.append(line)

# 나라 이름 추출 (첫 단어)
names = []
for line in countries:
    parts = line.split()
    names.append(parts[0])

# 이름 -> 인덱스 매핑
name_to_idx = {name: i for i, name in enumerate(names)}

# 그래프: origin -> destination
graph = [[] for _ in range(N)]

for line in countries:
    parts = line.split()
    dest = parts[0]
    # "allows travellers from"는 3개 단어, 그 이후가 origin 나라들
    origins = parts[4:]
    for origin in origins:
        graph[name_to_idx[origin]].append(name_to_idx[dest])

# BFS 초기화
visited = [0]*N
start = 0  # 첫 나라 index
visited[start] = 1  # 바이러스 퍼진 주차는 1주차

q = deque()
q.append(start)

while q:
    current = q.popleft()
    for nxt in graph[current]:
        if visited[nxt] == 0:
            visited[nxt] = visited[current] + 1
            q.append(nxt)

# 알파벳 순으로 출력
sorted_names = sorted(names)
for name in sorted_names:
    idx = name_to_idx[name]
    print(visited[idx])
