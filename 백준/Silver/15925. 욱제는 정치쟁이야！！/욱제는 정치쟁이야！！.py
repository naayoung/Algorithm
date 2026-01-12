import sys
input = sys.stdin.readline

input = sys.stdin.readline

n, target = map(int, input().split())
onoff = [list(map(int, input().split())) for _ in range(n)]

changed_any = True
check = 0  # 바꾼 행/열 개수 (누적)

while changed_any:
    changed_any = False

    # 행 반복
    for i in range(n):
        on_count = onoff[i].count(1)
        off_count = n - on_count

        if target == 1 and on_count > off_count:
            for j in range(n):
                if onoff[i][j] == 0:
                    onoff[i][j] = 1
                    changed_any = True
            if changed_any:
                check += 1

        elif target == 0 and off_count > on_count:
            for j in range(n):
                if onoff[i][j] == 1:
                    onoff[i][j] = 0
                    changed_any = True
            if changed_any:
                check += 1

    # 열 반복
    for i in range(n):
        on_count = 0
        for j in range(n):
            if onoff[j][i] == 1:
                on_count += 1
        off_count = n - on_count

        if target == 1 and on_count > off_count:
            for j in range(n):
                if onoff[j][i] == 0:
                    onoff[j][i] = 1
                    changed_any = True
            if changed_any:
                check += 1

        elif target == 0 and off_count > on_count:
            for j in range(n):
                if onoff[j][i] == 1:
                    onoff[j][i] = 0
                    changed_any = True
            if changed_any:
                check += 1

# 최종 판정
all_target = True
for row in onoff:
    for cell in row:
        if cell != target:
            all_target = False

print(1 if all_target else 0)