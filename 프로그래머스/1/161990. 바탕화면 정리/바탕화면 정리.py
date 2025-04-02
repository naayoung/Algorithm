def solution(wallpaper):
    answer = []
    max_x = len(wallpaper)
    max_y = len(wallpaper[0])
    tx, ty = [], []
    for x in range(max_x):
        for y in range(max_y):
            if wallpaper[x][y] == '#':
                tx.append(x)
                ty.append(y)
    answer.append(min(tx))
    answer.append(min(ty))
    
    answer.append(max(tx)+1)
    answer.append(max(ty)+1)
                    
    return answer