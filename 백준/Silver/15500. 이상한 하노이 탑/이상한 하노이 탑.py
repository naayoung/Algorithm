import sys
input = sys.stdin.readline

n = int(input().strip())
t = [[], [], []]                 # 1,2,3번 장대
t[0] = list(map(int, input().split()))  # 입력: 아래->위 순서, t[0][-1]이 맨 위

ans = []
pos = [0] * (n + 1)              # 각 원판의 현재 장대(1/2/3)
for x in t[0]:
    pos[x] = 1                   # 처음엔 전부 1번 장대

# 가장 큰 원판부터 차례로 3번 장대로 보낸다
for target in range(n, 0, -1):
    while True:
        p = pos[target]          # target이 있는 장대
        # target이 맨 위면 바로 3번으로
        if t[p-1] and t[p-1][-1] == target:
            t[p-1].pop()
            ans.append((p, 3))
            pos[target] = 3
            break
        # 아직 위에 다른 원판이 덮고 있으면 1<->2로만 치워서 위로 올린다
        if p == 1:
            x = t[0].pop()
            t[1].append(x)
            ans.append((1, 2))
            pos[x] = 2
        else:  # p == 2
            x = t[1].pop()
            t[0].append(x)
            ans.append((2, 1))
            pos[x] = 1

print(len(ans))
for a, b in ans:
    print(a, b)