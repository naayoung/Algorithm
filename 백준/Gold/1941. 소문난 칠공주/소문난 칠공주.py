import sys
input = sys.stdin.readline

def possible_next(selected):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    possible = set()

    for x, y in selected:
        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 5 and 0 <= ny < 5:
                if (nx, ny) not in selected:
                    possible.add((nx, ny))
    return list(possible)

def backtrack(selected, count_y):
    if count_y > 3:
        return
    if len(selected) == 7:
        key = tuple(sorted(selected))
        if key not in answers:
            answers.add(key)
        return

    for nx, ny in possible_next(selected):
        if (nx, ny) not in selected:
            selected.append((nx, ny))
            if girls[nx][ny] == 'Y':
                backtrack(selected, count_y+1)
            else:
                backtrack(selected, count_y)
            selected.remove((nx, ny))

girls = []
for _ in range(5):
    girls.append(list(input().strip()))

answers = set()
for i in range(5):
    for j in range(5):
        selected = set()
        selected = [(i, j)]
        if girls[i][j] == 'Y':
            backtrack(selected, 1)
        else:
            backtrack(selected, 0)
print(len(answers))