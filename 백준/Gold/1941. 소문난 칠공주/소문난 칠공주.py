import sys
input = sys.stdin.readline

# 상하좌우 이동
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 입력
girls = [list(input().strip()) for _ in range(5)]

ans = set()

def dfs(selected, count_y):
    if count_y > 3:
        return
    if len(selected) == 7:
        ans.add(tuple(sorted(selected)))
        return

    # 현재 선택한 좌표들의 인접 칸 탐색
    next_positions = set()
    for x, y in selected:
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if (nx, ny) not in selected:
                    next_positions.add((nx, ny))

    for nx, ny in next_positions:
        selected.add((nx, ny))
        dfs(selected, count_y + 1 if girls[nx][ny] == 'Y' else count_y)
        selected.remove((nx, ny))

# 모든 좌표에서 시작
for i in range(5):
    for j in range(5):
        start = {(i, j)}
        dfs(start, 1 if girls[i][j] == 'Y' else 0)

print(len(ans))