import sys
input = sys.stdin.readline

N = int(input().strip())
pizza = list(map(int, input().split()))

ans = [0] * N  # 각 학생의 완료 시간
cnt = 0        # 총 시간
tmp = [0] * N  # 각 학생이 받은 조각 수
done = [False] * N  # 완료 여부

while True:
    all_done = True  # 모든 학생 완료 여부

    for n in range(N):
        if not done[n]:  # 아직 다 안 먹은 학생만 처리
            tmp[n] += 1
            cnt += 1
            if tmp[n] == pizza[n]:
                ans[n] = cnt
                done[n] = True
            all_done = False  # 아직 남은 사람이 있음

    if all_done:
        print(*ans)
        break