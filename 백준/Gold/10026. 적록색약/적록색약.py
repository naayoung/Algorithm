import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input().strip())
graph = []
for _ in range(n):
    graph.append(list(input().strip()))
#방문 체크
visited = [[0] * n for _ in range(n)]

#범위 내 확인
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y, color, is_colorblind):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1:
        return False
    if is_colorblind:
        if color in ['R', 'G']:
            return graph[x][y] in ['R', 'G']
    return graph[x][y] == color

def dfs(x, y, color, is_colorblind):
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        
        if can_go(new_x, new_y, color, is_colorblind):
            visited[new_x][new_y] = 1
            dfs(new_x, new_y, graph[new_x][new_y], is_colorblind)

def count_regions(is_colorblind):
    global visited

    visited = [[0] * n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(i, j, graph[i][j], is_colorblind)
                count += 1
    return count

#적록색약이 아닌 경우
count_normal = count_regions(False)
#적록색약인 경우
count_blind = count_regions(True)

print(count_normal, count_blind)