import sys
input = sys.stdin.readline

def made(idx, a, b, c, d, m, chosen):
    global answer, best_combination

    if p <= a and f <= b and s <= c and v <= d:
        if m < answer:
            answer = m
            best_combination = chosen[:]

    if idx == n:
        return


    made(idx+1, a+nut[idx][0], b+nut[idx][1], c+nut[idx][2], d+nut[idx][3], m+nut[idx][4], chosen+[idx+1])
    made(idx+1, a, b, c, d, m, chosen)

n = int(input().strip())
p, f, s, v = map(int, input().split())
nut = [list(map(int, input().split())) for _ in range(n)]
answer = 9999999999
best_combination = []

made(0, 0, 0, 0, 0, 0, [])

if answer == 9999999999:
    print(-1)
else:
    print(answer)
    print(*best_combination)