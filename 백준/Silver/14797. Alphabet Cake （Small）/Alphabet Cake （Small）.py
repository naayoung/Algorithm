import sys
input = sys.stdin.readline

case = int(input().strip())
for ca in range(1, case+1):
    r, c = map(int, input().split())
    grid = [list(input().strip()) for _ in range(r)]

    # 가로 채우기
    for i in range(r):
        # 왼쪽에서 오른쪽
        for j in range(1, c):
            if grid[i][j] == '?' and grid[i][j-1] != '?':
                grid[i][j] = grid[i][j-1]
        # 오른쪽에서 왼쪽
        for j in range(c-2, -1, -1):
            if grid[i][j] == '?' and grid[i][j+1] != '?':
                grid[i][j] = grid[i][j+1]

    # 세로 채우기 (위→아래)
    for i in range(1, r):
        if all(ch == '?' for ch in grid[i]) and any(ch != '?' for ch in grid[i-1]):
            grid[i] = grid[i-1][:]
    # 세로 채우기 (아래→위)
    for i in range(r-2, -1, -1):
        if all(ch == '?' for ch in grid[i]) and any(ch != '?' for ch in grid[i+1]):
            grid[i] = grid[i+1][:]

    print("Case #"+str(ca)+":")
    for i in range(r):
        print("".join(grid[i]))
