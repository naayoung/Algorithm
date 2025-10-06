import sys
input = sys.stdin.readline

while True:
    S = int(input().strip())
    cnt = {}

    if S == 0:
        break

    for s in range(S):
        courses = tuple(sorted(map(int, input().split())))
        cnt[courses] = cnt.get(courses, 0)+1

    mx = max(cnt.values())
    answer = 0
    for v in cnt.values():
        if v == mx:
            answer += v

    print(answer)