import sys
input = sys.stdin.readline

n = int(input().strip())
graph = [list(map(int, input().strip())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

count = 0
town = []

#범위 안에 위치해 있는 지 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

#방문한 곳인지, 집이 있는 곳인지 확인
def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or graph[x][y] == 0:
        return False
    
    return True

def dfs(x, y):
    global count

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            count += 1
            visited[new_x][new_y] = 1

            dfs(new_x, new_y)

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            count = 1
            visited[i][j] = 1

            dfs(i, j)

            #탐색 끝나면 입력
            town.append(count)

#답안
town.sort()
print(len(town))
for i in town:
    print(i)