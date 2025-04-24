from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 도달할 수 있는 최대 값은 N + N//2 (이를 넘지 않도록 설정)
MAX = N + N // 2 + 1

# dp 배열: dp[i]는 i번째 계단에 도달할 때 최소 K번 이하로 도달할 수 있는 횟수
dp = [float('inf')] * MAX
dp[0] = 0  # 처음에는 0번 계단에 0번으로 도달

# BFS
queue = deque([0])  # 시작점은 0
while queue:
    cur = queue.popleft()
    for next_step in [cur + 1, cur + cur // 2]:  # +1, +현재//2
        if next_step < MAX and dp[next_step] > dp[cur] + 1:
            dp[next_step] = dp[cur] + 1
            queue.append(next_step)

# dp[N]이 K 이하이면 minigimbob, 아니면 water
if dp[N] <= K:
    print("minigimbob")
else:
    print("water")